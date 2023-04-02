import re
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    words = nltk.word_tokenize(text)
    words = [word.lower() for word in words if word.lower() not in stop_words]
    return ' '.join(words)


def remove_emojis(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  
        u"\U0001F300-\U0001F5FF"  
        u"\U0001F680-\U0001F6FF"  
        u"\U0001F1E0-\U0001F1FF"  
        u"\U00002702-\U000027B0"  
        u"\U000024C2-\U0001F251"  
        u"\U0001F900-\U0001F9FF"  
        u"\U0001F1F2-\U0001F1F4"  
        u"\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002702-\U000027B0\U000024C2-\U0001F251\U0001F900-\U0001F9FF"  # new emojis
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


if __name__ == "__main__":
    text = "I am anmol khandelwal 😂"
    text = remove_emojis(text)
    text = remove_stopwords(text)
    print(text)
    