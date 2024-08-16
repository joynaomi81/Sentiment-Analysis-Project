import nltk
import streamlit as st
import pickle
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

st.title('Movie Reviews Sentiment Analysis App')

# Input text box
review = st.text_area('Enter your movie review:', '')

# Button to perform sentiment analysis
if st.button('Review'):
    if review:
        # Perform sentiment analysis
        scores = analyzer.polarity_scores(review)


        # Provide an overall sentiment based on the compound score
        if scores['compound'] >= 0.05:
            st.success('This comment is: Positive')
        elif scores['compound'] <= -0.05:
            st.error('This comment is: Negative')
        else:
            st.warning('This comment is: Neutral')
    else:
        st.write('Please enter a review to analyze.')

    
