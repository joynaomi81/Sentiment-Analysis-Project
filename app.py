import nltk
import streamlit as st
import joblib
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

def output(input_text):
    analyzer = SentimentIntensityAnalyzer()
    prediction = analyzer.polarity_scores(input_text)
    
    # Classification based on sentiment scores
    if prediction['neg'] > prediction['pos'] and prediction['neg'] > prediction['neu']:
        text = 'This comment is bad'
    elif prediction['pos'] > prediction['neg'] and prediction['pos'] > prediction['neu']:
        text = 'This comment is good'
    else:
        text = 'This comment is neither good nor bad'

    return text

# Example usage
comment = "Your example text here."
result = output(comment)
print(result)


