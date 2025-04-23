from tensorflow.keras.preprocessing.text import Tokenizer
import pickle
import pandas as pd
import os

# Create models directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Initialize a tokenizer
tokenizer = Tokenizer(num_words=5000)

# If you have your processed data available, fit the tokenizer
try:
    # Try to load the processed data
    processed_data = pd.read_csv("../data/processed_reviews.csv")
    print(f"Fitting tokenizer on {len(processed_data)} reviews")
    tokenizer.fit_on_texts(processed_data['cleaned_review'].values)
except Exception as e:
    print(f"Could not load processed data: {e}")
    # Fit on dummy data if needed
    tokenizer.fit_on_texts(["this is a sample movie review to initialize the tokenizer"])
    print("Fitted tokenizer on sample data")

# Save the tokenizer
with open("models/tokenizer.pickle", "wb") as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
print(f"Tokenizer saved to {os.path.abspath('models/tokenizer.pickle')}")