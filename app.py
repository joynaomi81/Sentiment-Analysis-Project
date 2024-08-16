import nltk
import streamlit as st
import pickle
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
    


def output(input):
    analyzer = SentimentIntensityAnalyzer()
    prediction = analyzer.polarity_scores(input)
    text = ""
    if prediction['neg']>=0.5 and prediction['neu']<=0.49 and prediction['pos']<=0.49:
        text='This comment is Negative'
    elif prediction['neg']<=0.49 and prediction['neu']>=0.50 and prediction['pos']<=0.49:
        text='This comment is neither positive nor negative'
    elif prediction['neg']<=0.49 and prediction['neu']<=0.49 and prediction['pos']>=0.50:
        text = 'This comment is Positive'

    return text



st.title('Sentiment Analysis App')
input = st.text_input('Enter Your Phrase Here')
final_display = ""
if st.button('Check Review'):
    final_display = output(input)
    st.success(final_display)

