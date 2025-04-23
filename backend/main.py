from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, List
import joblib
import tensorflow as tf
from transformers import pipeline
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import pickle
import numpy as np
import json
import os

# Import utility functions
from utils.preprocess import preprocess_text
from utils.ensemble import ensemble_prediction, predict_logistic_regression, predict_lstm, transformer_predict
from database.mongodb import save_review, save_user

# Initialize FastAPI app
app = FastAPI(title="Movie Review Sentiment Analysis API")

# Add CORS middleware to allow cross-origin requests from the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load models using absolute paths
try:
    # Get the current script directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(base_dir, "models")
    
    print(f"Looking for models in: {models_dir}")
    print(f"Files in models directory: {os.listdir(models_dir)}")
    
    # Load models with absolute paths
    vectorizer = joblib.load(os.path.join(models_dir, "vectorizer.pkl"))
    lr_model = joblib.load(os.path.join(models_dir, "sentiment_model.pkl"))
    lstm_model = tf.keras.models.load_model(os.path.join(models_dir, "lstm_model.h5"))
    
    # Load tokenizer
    tokenizer_path = os.path.join(models_dir, "tokenizer.pickle")
    print(f"Loading tokenizer from: {tokenizer_path}")
    with open(tokenizer_path, "rb") as handle:
        tokenizer = pickle.load(handle)
    
    # Initialize transformer model
    transformer_model = pipeline("sentiment-analysis")
    
    print("All models loaded successfully!")
    print(f"Tokenizer type: {type(tokenizer)}")
    print(f"LSTM model type: {type(lstm_model)}")
    print(f"Vectorizer type: {type(vectorizer)}")
except Exception as e:
    print(f"Error loading models: {e}")
    raise

# Define request and response models
class ReviewRequest(BaseModel):
    review_text: str
    user_id: Optional[str] = None

class SentimentResponse(BaseModel):
    review_text: str
    sentiment: str
    confidence: float
    model_breakdown: Dict[str, Dict[str, float]]
    themes: List[str]

@app.get("/")
def read_root():
    return {"message": "Welcome to Movie Review Sentiment Analysis API"}

@app.post("/analyze/", response_model=SentimentResponse)
async def analyze_review(review_request: ReviewRequest):
    try:
        # Get review text
        review_text = review_request.review_text
        
        if not review_text or len(review_text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Review text cannot be empty")
        
        # Print debug info
        print(f"Review text: {review_text[:50]}...")
        
        # Preprocess the text
        cleaned_text = preprocess_text(review_text)
        
        # Get individual model predictions
        # 1. Logistic Regression
        try:
            lr_sentiment = predict_logistic_regression(cleaned_text, vectorizer, lr_model)
            lr_proba = lr_model.predict_proba(vectorizer.transform([cleaned_text]))[0]
            lr_confidence = lr_proba[1] if lr_sentiment == "positive" else lr_proba[0]
        except Exception as e:
            print(f"Error in logistic regression prediction: {e}")
            lr_sentiment = "neutral"
            lr_confidence = 0.5
        
        # 2. LSTM
        try:
            # Explicitly pass the tokenizer to the predict function
            lstm_sentiment = predict_lstm(cleaned_text, tokenizer, lstm_model)
            lstm_sequence = tokenizer.texts_to_sequences([cleaned_text])
            padded_sequence = pad_sequences(lstm_sequence, maxlen=100)
            
            # Try with default predict
            try:
                lstm_prediction = lstm_model.predict(padded_sequence, verbose=0)[0][0]
            except Exception as e:
                print(f"LSTM predict error: {e}")
                # Try alternative approach
                lstm_prediction = lstm_model(padded_sequence, training=False).numpy()[0][0]
                
            lstm_confidence = float(lstm_prediction) if lstm_sentiment == "positive" else 1.0 - float(lstm_prediction)
        except Exception as e:
            print(f"Error in LSTM prediction: {e}")
            lstm_sentiment = lr_sentiment  # Fallback to logistic regression
            lstm_confidence = 0.5
        
        # 3. Transformer
        try:
            transformer_sentiment, transformer_confidence = transformer_predict(review_text, transformer_model)
        except Exception as e:
            print(f"Error in transformer prediction: {e}")
            transformer_sentiment = "neutral"
            transformer_confidence = 0.5
        
        # Combine predictions using ensemble method
        predictions = [lr_sentiment, lstm_sentiment, transformer_sentiment]
        confidences = [lr_confidence, lstm_confidence, transformer_confidence]
        
        print(f"Predictions: {predictions}")
        print(f"Confidences: {confidences}")
        
        final_sentiment = max(set(predictions), key=predictions.count)
        
        # Calculate confidence by averaging confidences of models that agree with final sentiment
        matching_confidences = [conf for pred, conf in zip(predictions, confidences) if pred == final_sentiment]
        final_confidence = sum(matching_confidences) / len(matching_confidences) if matching_confidences else 0.5
        
        # Extract themes (genres) based on keywords in the text
        themes = []
        genres = {
            "Action": ["action", "fight", "explosion", "chase", "thrill", "adventure"],
            "Drama": ["drama", "emotion", "intense", "relationship", "conflict", "struggle"],
            "Comedy": ["comedy", "funny", "humor", "laugh", "joke", "hilarious"],
            "Horror": ["horror", "scary", "terrifying", "fear", "creepy", "nightmare"],
            "Romance": ["romance", "love", "relationship", "romantic", "passion", "couple"],
            "SciFi": ["science fiction", "sci-fi", "future", "alien", "space", "technology"],
            "Fantasy": ["fantasy", "magical", "dragon", "wizard", "mythical", "enchanted"],
            "Thriller": ["thriller", "suspense", "tension", "mystery", "twist", "intense"]
        }
        
        for genre, keywords in genres.items():
            if any(keyword in cleaned_text for keyword in keywords):
                themes.append(genre)
        
        # If no themes detected, add "General" as a fallback
        if not themes:
            themes.append("General")
        
        # Create model breakdown dictionary
        model_breakdown = {
            "logistic_regression": {
                "sentiment": lr_sentiment,
                "confidence": float(lr_confidence)
            },
            "lstm": {
                "sentiment": lstm_sentiment,
                "confidence": float(lstm_confidence)
            },
            "transformer": {
                "sentiment": transformer_sentiment,
                "confidence": float(transformer_confidence)
            }
        }
        
        # Save review to database if user_id is provided
        if review_request.user_id:
            review_data = {
                "user_id": review_request.user_id,
                "review_text": review_text,
                "sentiment": final_sentiment,
                "themes": themes,
                "model_breakdown": model_breakdown
            }
            save_review(review_data)
        
        # Return response
        return SentimentResponse(
            review_text=review_text,
            sentiment=final_sentiment,
            confidence=final_confidence,
            model_breakdown=model_breakdown,
            themes=themes
        )
    
    except Exception as e:
        print(f"Error analyzing review: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error analyzing review: {str(e)}")

# Additional routes for user management
class UserCreate(BaseModel):
    username: str
    email: str
    password: str  # In production, ensure this is securely hashed
    preferences: Optional[List[str]] = []

@app.post("/users/")
async def create_user(user: UserCreate):
    try:
        user_id = save_user(user.dict())
        return {"message": "User created successfully", "user_id": str(user_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the app (for development only - use uvicorn in production)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)