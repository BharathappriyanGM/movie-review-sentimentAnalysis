# Save this as create_tokenizer.py in your backend folder
import pandas as pd
import pickle
from keras.preprocessing.text import Tokenizer

# Load your processed data
processed_data_path = "D:/Engineering Files/FYP/Movie Review Project/processed_reviews.csv"
df = pd.read_csv(processed_data_path)

print(f"Loaded {len(df)} reviews from processed data")

# Create and fit the tokenizer
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(df['cleaned_review'].values)

print(f"Fitted tokenizer with vocabulary size: {len(tokenizer.word_index)}")

# Save the tokenizer
with open("models/tokenizer.pickle", "wb") as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("Tokenizer saved to models/tokenizer.pickle")
print("Tokenizer saved to models/tokenizer.pickle")