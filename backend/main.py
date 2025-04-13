from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from utils.preprocess import preprocess_text
from utils.ensemble import ensemble_prediction

# Initialize FastAPI app
app = FastAPI()

# Load models and vectorizer
vectorizer = joblib.load("./models/vectorizer.pkl")
lr_model = joblib.load("./models/sentiment_model.pkl")

@app.get("/")
def home():
    return {"message": "Welcome to Movie Review Analyzer API"}

@app.post("/analyze/")
def analyze_review(review: str):
    try:
        sentiment = ensemble_prediction(review, vectorizer, lr_model)  # Combine predictions.
        return {"review": review, "sentiment": sentiment}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
