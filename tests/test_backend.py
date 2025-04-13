import pytest
from fastapi.testclient import TestClient
from main import app

# Initialize FastAPI test client
client = TestClient(app)

# Test the homepage
def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Movie Review Analyzer API"}

# Test user registration
def test_register_user():
    user_data = {
        "username": "test_user",
        "email": "test@example.com",
        "password": "securepassword",
        "preferences": ["Action", "Drama"]
    }
    response = client.post("/register/", json=user_data)
    assert response.status_code == 200
    assert "user_id" in response.json()

# Test review submission
def test_submit_review():
    review_data = {
        "user_id": "12345",
        "review_text": "Amazing storyline and great acting!",
        "sentiment": "positive"
    }
    response = client.post("/submit_review/", json=review_data)
    assert response.status_code == 200
    assert "review_id" in response.json()

# Test ensemble analysis
def test_analyze_review():
    payload = {
        "review": "Fantastic movie with wonderful performances!",
        "user_id": "12345"
    }
    response = client.post("/analyze/", json=payload)
    assert response.status_code == 200
    assert "sentiment" in response.json()
