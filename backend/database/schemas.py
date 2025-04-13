from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict

# Schema for user data
class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str  # In production, passwords should be securely hashed
    preferences: Optional[List[str]] = []  # List of preferred genres (e.g., ['Action', 'Drama'])

# Schema for user reviews
class ReviewSchema(BaseModel):
    user_id: str  # ID of the user submitting the review
    review_text: str  # The text of the movie review
    sentiment: str  # Sentiment of the review ('positive' or 'negative')
    themes: Optional[Dict[str, float]] = {}  # Thematic breakdown (e.g., {'Action': 60.0, 'Drama': 40.0})
