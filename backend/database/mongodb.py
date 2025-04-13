from pymongo import MongoClient

# MongoDB Atlas or localhost connection URI
MONGO_URI = "mongodb://localhost:27017/"

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Access your project database
db = client.priyanmoviereview  # Your newly created database

# Collections
users_collection = db.users
reviews_collection = db.reviews

# Example function to save user data
def save_user(user_data):
    try:
        result = users_collection.insert_one(user_data)
        return result.inserted_id
    except Exception as e:
        raise Exception(f"Failed to save user: {e}")

# Example function to save review data
def save_review(review_data):
    result = reviews_collection.insert_one(review_data)
    return result.inserted_id
