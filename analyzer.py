from textblob import TextBlob
import re

def getScore(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity,subjectivity

def remove_emojis(text):
    # regular expression pattern to match emojis
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"  # dingbats
        u"\U000024C2-\U0001F251"  # enclosed characters
        u"\U0001F900-\U0001F9FF"  # supplemental symbols and pictographs
        u"\U0001F1F2-\U0001F1F4"  # country flags with high Unicode values
        u"\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002702-\U000027B0\U000024C2-\U0001F251\U0001F900-\U0001F9FF"  # new emojis
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

if __name__ == "__main__":
    limit = 150
    for i in range(limit):
        file_name = f"Reviews/review_{i}.txt"
        with open(file_name,"r",encoding = "utf-8") as F:
            # pol,sub = getScore(F.read())
            text = F.read()
            text = remove_emojis(text)
            print(i,text,end="\n---------------------\n")
