import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze(text):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    return scores

if __name__ == "__main__":
    
    