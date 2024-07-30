
import streamlit as st
import joblib
import os

# Define the path to the model file
model_path = 'sentiment_model.pkl'

# Check if the file exists
if os.path.exists(model_path):
    # Load the trained model
    model = joblib.load(model_path)
else:
    # Display an error message
    st.error(f"Model file '{model_path}' not found. Please ensure the file is in the correct location.")
    st.stop()  # Stop the script execution

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

# Instructions for the user
st.write("""
### Instructions:
- Enter a movie review in the text area above.
- Click the 'Analyze Sentiment' button to see the predicted sentiment.
""")
