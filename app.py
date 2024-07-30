import streamlit as st
import joblib

# Load the trained model
model = joblib.load('sentiment_model.pkl')

# Title of the app
st.title('Movie Reviews Sentiment Analysis')

# Input for the user to enter a movie review
user_input = st.text_area('Enter a movie review:', '')

# Button for making prediction
if st.button('Analyze Sentiment'):
    if user_input:
        # Predict sentiment
        prediction = model.predict([user_input])[0]
        # Display the result
        st.write(f'The sentiment of the review is: {prediction}')
    else:
        st.write('Please enter a review to analyze.')


st.write("""
### Instructions:
- Enter a movie review in the text area above.
- Click the 'Analyze Sentiment' button to see the predicted sentiment.
""")
