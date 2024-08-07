import streamlit as st
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Load the model and vectorizer from the files
def load_model():
    with open('model.pkl', 'rb') as model_file, open('cv-vectorizer.pkl', 'rb') as vectorizer_file:
        model = pickle.load(model_file)
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

# Function to predict sentiment
def predict_sentiment(text, model, vectorizer):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return 'Positive' if prediction[0] == 1 else 'Negative'

# Main function to run the Streamlit app
def main():
    st.title("Sentiment Analysis App")
    st.write("Enter a movie review and get the sentiment prediction:")

    # Input text box for user to enter movie review
    user_input = st.text_area("Enter your review here:")

    if st.button("Predict"):
        if user_input:
            model, vectorizer = load_model()
            prediction = predict_sentiment(user

