import numpy as np
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

from clean import preprocess_text

def analyze(text):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    scores = scores["compound"]
    score_out_of_5 = (scores + 1) * 2.5
    return score_out_of_5

if __name__ == "__main__":
    actual_stars = []
    nlp_score = []
    df = pd.read_csv("reviews.csv")
    
    for k,v in df.iterrows():
        text = v['review']
        print(text)
        text = preprocess_text(text)
        try:
            nlp_scr = analyze(text)
        except:
            pass
        stars = v['stars']
        print(text)
        print(nlp_scr,stars)
        actual_stars.append(stars)
        nlp_score.append(nlp_scr)
        print("\n-------------------\n")

    # corr_coef = np.corrcoef(actual_stars, nlp_score)[0, 1]
    # print(corr_coef)
