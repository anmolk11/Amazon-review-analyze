import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# from spellchecker import SpellChecker

def preprocess_text(text):
    # Tokenize the text
    words = nltk.word_tokenize(text)
    
    # Convert to lowercase
    words = [word.lower() for word in words]
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # Remove special characters and numbers
    words = [re.sub(r'[^a-zA-Z0-9]', '', word) for word in words]
    
    # Spell correction
    # spell = SpellChecker()
    # words = [spell.correction(word) for word in words]
    
    # Join the words back into a string
    text = ' '.join(words)
    
    return text



if __name__ == "__main__":
    text = "I am anmol khandelwal 😂"
    text = preprocess_text(text)
    print(text)
    