import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
nltk.download('punkt')       # Tokenizer
nltk.download('stopwords')   # Stopwords
nltk.download('wordnet')     # Lemmatization dictionary

def preprocess_text(text):
    """
    Preprocess a given text:
    1. Convert to lowercase.
    2. Remove non-alphabetical characters.
    3. Tokenize the text.
    4. Remove stopwords.
    5. Lemmatize the words.
    """
    if not isinstance(text, str):  # Return empty string if text is invalid
        return ""

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
    
    # Join the processed words back into a single string
    return ' '.join(words)

def preprocess_dataset(df):
    """
    Apply preprocessing to the dataset:
    - Clean the 'review' column.
    - Handle missing values.
    - Map sentiment labels to binary values (positive -> 1, negative -> 0).
    """
    # Handle missing reviews by replacing NaN with an empty string
    df['review'] = df['review'].fillna("")
    
    # Apply the preprocess_text function to the 'review' column
    df['cleaned_review'] = df['review'].apply(preprocess_text)
    
    # Map sentiment labels to 1 (positive) and 0 (negative)
    df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})
    
    return df
