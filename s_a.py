import pandas as pd
import re
import nltk
nltk.data.path.append(r'D:\Engineering Files\FYP\Movie Review Project\nltk_data')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Dataset
def load_dataset(file_path):
    # Load dataset with proper encoding
    df = pd.read_csv(file_path, encoding='latin1')  # Change encoding if needed
    print("Dataset Loaded Successfully!")
    print(df.head())
    return df

# Step 2: Text Preprocessing
def preprocess_text(text):
    if not isinstance(text, str):
        return ""  # Return empty string if not a valid string

    # Convert to lowercase
    text = text.lower()
    # Remove non-alphabetical characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenize the text
    words = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    return ' '.join(words)

# Step 3: Preprocessing Function
def preprocess_dataset(df):
    nltk.download('punkt')  # Sentence tokenizer
    nltk.download('stopwords')  # Stopwords for removing unnecessary words
    nltk.download('wordnet')  # Lemmatization dictionary

    # Handle NaN or None values in the review column
    df['review'] = df['review'].fillna("")  # Replace NaN with empty string

    # Apply text preprocessing to the 'review' column
    df['cleaned_review'] = df['review'].apply(preprocess_text)
    # Map sentiment to binary values
    df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})
    
    return df

# Step 4: Feature Extraction Using TF-IDF
def vectorize_data(df):
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(df['cleaned_review']).toarray()
    y = df['sentiment']
    print("Feature Extraction Completed!")
    return X, y, vectorizer

# Step 5: Train-Test Split
def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Train-Test Split: {X_train.shape}, {X_test.shape}")
    return X_train, X_test, y_train, y_test

# Step 6: Train the Logistic Regression Model
def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    print("Model Training Completed!")
    return model

# Step 7: Evaluate the Model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    return y_pred

# Step 8: Save the Model and Vectorizer
def save_model_and_data(model, vectorizer, df):
    joblib.dump(model, "sentiment_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")
    df.to_csv("processed_reviews.csv", index=False)
    print("Model and Preprocessed Data Saved!")

# Step 9: Visualize Metrics
def visualize_metrics(y_test, y_pred):
    from sklearn.metrics import precision_score, recall_score, f1_score
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-score']
    values = [
        accuracy_score(y_test, y_pred),
        precision_score(y_test, y_pred),
        recall_score(y_test, y_pred),
        f1_score(y_test, y_pred)
    ]
    plt.figure(figsize=(8, 6))
    sns.barplot(x=metrics, y=values)
    plt.title("Model Evaluation Metrics")
    plt.ylim(0, 1)
    plt.show()

# Main Function
if __name__ == "__main__":
    # Path to your dataset
    dataset_path = r"D:\Engineering Files\FYP\Movie Review Project\Dataset.csv"

    # Load dataset
    df = load_dataset(dataset_path)

    # Preprocess dataset
    df = preprocess_dataset(df)

    # Feature extraction and splitting
    X, y, vectorizer = vectorize_data(df)
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Train model
    model = train_model(X_train, y_train)

    # Evaluate model
    y_pred = evaluate_model(model, X_test, y_test)

    # Save model and data
    save_model_and_data(model, vectorizer, df)

    # Visualize evaluation metrics
    visualize_metrics(y_test, y_pred)
