import streamlit as st
import joblib

# Load the trained model
model = joblib.load('model.pkl')  
# Title of the app
st.title("Sentiment Analysis App")

# Text input from the user
user_input = st.text_input("Enter a text here:")

# Predict button
if st.button("Predict"):
    if user_input:
        # Make prediction
        prediction = model.predict([user_input])
        
        # print the result
        sentiment = "Positive" if prediction[0] == 1 else "Negative"
        st.write(f'Sentiment: {sentiment}')
    else:
        st.write("Please enter text to analyze.")

