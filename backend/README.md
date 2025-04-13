# Backend for Movie Review Analyzer

## Overview
This backend is built using FastAPI and MongoDB. It handles user authentication, review sentiment analysis, and thematic breakdown using a combination of machine learning models (Logistic Regression, LSTM, Hugging Face Transformers).

## Features
- **User Registration**: Store user details (name, email, preferences) in MongoDB.
- **Sentiment Analysis**: Analyze reviews to determine positive or negative sentiment.
- **Thematic Breakdown**: Extract themes (Action, Drama, Sci-Fi, etc.) from reviews.
- **Review History**: Save user-submitted reviews and sentiment analysis results.

## Project Structure
MovieReviewProject/
│
├── backend/                  # Backend folder
│   ├── main.py               # FastAPI main application
│   ├── models/               # Machine learning models
│   │   ├── lstm_model.h5     # Trained LSTM model
│   │   ├── sentiment_model.pkl # Logistic Regression model
│   │   ├── vectorizer.pkl    # TF-IDF vectorizer
│   ├── utils/                # Utility functions for the backend
│   │   ├── preprocess.py     # Text preprocessing functions
│   │   ├── ensemble.py       # Ensemble prediction logic
│   ├── database/             # Database connection files
│   │   ├── mongodb.py        # MongoDB connection and CRUD operations
│   │   ├── schemas.py        # User and review data schemas
│   ├── requirements.txt      # Python dependencies
│   └── README.md             # Documentation for backend
│
├── frontend/                 # Frontend folder
│   ├── public/               # Static files (images, icons, etc.)
│   ├── src/                  # Source folder
│   │   ├── components/       # Reusable React components
│   │   │   ├── Navbar.js     # Navigation bar
│   │   │   ├── Dashboard.js  # User dashboard page
│   │   │   ├── AdminPanel.js # Admin panel page
│   │   │   ├── Analyzer.js   # Sentiment analysis page
│   │   └── services/         # API service files
│   │       ├── api.js        # Axios API calls to FastAPI
│   ├── package.json          # Frontend dependencies
│   └── README.md             # Documentation for frontend
│
├── data/                     # Dataset folder
│   ├── Dataset.csv           # Original dataset file
│   ├── processed_reviews.csv # Preprocessed dataset
│
├── logs/                     # Logs folder
│   ├── app.log               # Logs for debugging and tracking
│
├── tests/                    # Tests folder
│   ├── test_backend.py       # Automated tests for backend
│   ├── test_frontend.js      # Automated tests for frontend
│
├── .gitignore                # Git ignored files
├── docker-compose.yml        # Docker setup for full-stack deployment
├── README.md                 # Project overview and instructions
└── LICENSE                   # License for the project


## Prerequisites
Before running this project, ensure you have:
- Python 3.7 to 3.10 installed.
- MongoDB (local or Atlas) set up.
- Required Python dependencies installed (`requirements.txt`).

## Setup
1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd MovieReviewProject/backend
2. Install dependencies:
    pip install -r requirements.txt
3. Update the MongoDB connection URI in database/mongodb.py:
    MONGO_URI = "mongodb+srv://<username>:<password>@cluster-url.mongodb.net/"
4. Run the server:
    uvicorn main:app --reload
