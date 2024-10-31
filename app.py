import streamlit as st
import joblib

# Load the trained model
model = joblib.load('model.pkj')  # Ensure this path is correct

# Title of the app
st.title("Sentiment Analysis App")

# Text input from the user
user_input = st.text_input("Enter text here:")

# Predict button
if st.button("Predict"):
    if user_input:
        # Make prediction
        prediction = model.predict([user_input])

        # Display result with emoji
        if prediction[0] == 1:
            sentiment = "Positive 😊"
        else:
            sentiment = "Negative 😞"
        
        st.write(f'Sentiment: {sentiment}')
    else:
        st.write("Please enter text to analyze.")
