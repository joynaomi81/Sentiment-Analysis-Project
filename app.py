import streamlit as st
import joblib

# Load the trained model and TF-IDF vectorizer
model = joblib.load('model.pkj')  # This should be the path where you saved your model

# Title of the app
st.title("Sentiment Analysis App")

# Text input from the user
user_input = st.text_input("Enter a text for sentiment analysis:")

# Predict button
if st.button("Predict"):
    if user_input:
        # Make prediction
        prediction = model.predict([user_input])
        
        # Display the result
        sentiment = "Positive" if prediction[0] == 1 else "Negative"
        st.write(f'Sentiment: {sentiment}')
    else:
        st.write("Please enter text to analyze.")

