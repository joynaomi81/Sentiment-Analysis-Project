mport nltk
import streamlit as st
import pickle
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# Load your pre-trained sentiment analysis model
# Example with SentimentIntensityAnalyzer:
analyzer = SentimentIntensityAnalyzer()

# If you have a custom model, load it like this:
# with open('path_to_your_model.pkl', 'rb') as model_file:
#     analyzer = pickle.load(model_file)

# Title of the app
st.title('Movie Reviews Sentiment Analysis')

# Input text box
review = st.text_area('Enter your movie review:', '')

# Button to perform sentiment analysis
if st.button('Analyze Sentiment'):
    if review:
        # Perform sentiment analysis
        scores = analyzer.polarity_scores(review)

        # Display the results
        st.write('**Sentiment Analysis Results:**')
        st.write(f"Negative: {scores['neg']:.3f}")
        st.write(f"Neutral: {scores['neu']:.3f}")
        st.write(f"Positive: {scores['pos']:.3f}")
        st.write(f"Compound: {scores['compound']:.3f}")

        # Provide an overall sentiment based on the compound score
        if scores['compound'] >= 0.05:
            st.success('Overall Sentiment: Positive')
        elif scores['compound'] <= -0.05:
            st.error('Overall Sentiment: Negative')
        else:
            st.warning('Overall Sentiment: Neutral')
    else:
        st.write('Please enter a review to analyze.')

    
