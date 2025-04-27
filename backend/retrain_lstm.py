import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os

print("TensorFlow version:", tf.__version__)

# Set up paths
base_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(base_dir, "models")
data_dir = os.path.join(os.path.dirname(base_dir), "data")
os.makedirs(models_dir, exist_ok=True)

# Load your processed dataset
try:
    # Try different possible locations for the processed data
    possible_paths = [
        os.path.join(data_dir, "processed_reviews.csv"),
        os.path.join(os.path.dirname(data_dir), "processed_reviews.csv"),
        "../data/processed_reviews.csv",
        "../../data/processed_reviews.csv",
        "processed_reviews.csv"
    ]
    
    df = None
    for path in possible_paths:
        try:
            print(f"Trying to load data from {path}")
            if os.path.exists(path):
                df = pd.read_csv(path)
                print(f"Successfully loaded {len(df)} rows from {path}")
                break
        except Exception as e:
            print(f"Could not load from {path}: {e}")
    
    if df is None:
        # Create a small synthetic dataset as fallback
        print("Could not load the dataset, creating synthetic data for testing")
        reviews = [
            "This movie was amazing and brilliant",
            "Terrible film with bad acting",
            "I loved everything about this movie",
            "Worst film I've ever seen"
        ]
        sentiments = [1, 0, 1, 0]  # 1 for positive, 0 for negative
        df = pd.DataFrame({
            'cleaned_review': reviews,
            'sentiment': sentiments
        })
    
    # Create and fit tokenizer
    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(df['cleaned_review'].values)
    
    # Save tokenizer
    tokenizer_path = os.path.join(models_dir, "tokenizer.pickle")
    with open(tokenizer_path, "wb") as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"Tokenizer saved to {tokenizer_path}")
    
    # Prepare sequences
    X_sequences = tokenizer.texts_to_sequences(df['cleaned_review'].values)
    X_padded = pad_sequences(X_sequences, maxlen=100)
    y = df['sentiment'].values
    
    # Create a new LSTM model
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=5000, output_dim=128, input_length=100),
        tf.keras.layers.LSTM(128, dropout=0.2),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    # Train the model (use a subset for speed if dataset is large)
    sample_size = min(10000, len(X_padded))
    indices = np.random.choice(len(X_padded), sample_size, replace=False)
    
    print(f"Training on {sample_size} samples...")
    model.fit(
        X_padded[indices], 
        y[indices],
        batch_size=32,
        epochs=3,  # Quick training for demonstration
        validation_split=0.2
    )
    
    # Save the model
    model_path = os.path.join(models_dir, "lstm_model.h5")
    model.save(model_path)
    print(f"LSTM model saved to {model_path}")
    
except Exception as e:
    print(f"Error in LSTM training: {e}")
    raise