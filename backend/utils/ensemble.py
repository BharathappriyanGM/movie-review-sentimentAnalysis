from transformers import pipeline
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences


def transformer_predict(review):
    """
    Predict sentiment using a Hugging Face Transformer pipeline.
    """
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(review)
    return result[0]['label'].lower(), result[0]['score']  # Convert labels to lowercase

def predict_logistic_regression(review, vectorizer, model):
    """
    Predict sentiment using the Logistic Regression model.
    """
    # Transform review into TF-IDF features
    review_features = vectorizer.transform([review]).toarray()
    prediction = model.predict(review_features)
    return "positive" if prediction[0] == 1 else "negative"

def predict_lstm(review, tokenizer, lstm_model):
    """
    Predict sentiment using the LSTM model.
    """
    from tensorflow.keras.preprocessing.sequence import pad_sequences

    # Tokenize and pad the review
    sequence = tokenizer.texts_to_sequences([review])
    padded_sequence = pad_sequences(sequence, maxlen=100)
    
    # Get the prediction from the LSTM model
    prediction = lstm_model.predict(padded_sequence)[0][0]
    return "positive" if prediction > 0.5 else "negative"

def ensemble_prediction(review, vectorizer, lr_model, lstm_model, tokenizer):
    """
    Combine predictions from Logistic Regression, LSTM, and Transformers:
    - Majority voting is used for the final prediction.
    """
    # Get individual predictions
    lr_sentiment = predict_logistic_regression(review, vectorizer, lr_model)
    lstm_sentiment = predict_lstm(review, tokenizer, lstm_model)
    transformer_sentiment, confidence = transformer_predict(review)
    
    # Combine predictions (Majority vote)
    predictions = [lr_sentiment, lstm_sentiment, transformer_sentiment]
    final_prediction = max(set(predictions), key=predictions.count)
    
    return final_prediction
