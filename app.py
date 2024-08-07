import streamlit as st
import pickle
import os

# Print current working directory
print("/content/cv-vectorzier.plk:", os.getcwd())

# List files in the current working directory
print("Files in the current working directory:", os.listdir())

# Load the CountVectorizer and model from pickle files
save_cv = pickle.load(open('cv-vectorizer.pkl', 'rb'))
model = pickle.load(open('Movie_Reviews_Sentiment_Analysis.pkl', 'rb'))

def predict_sentiment(text):
    """Predict the sentiment of the input text."""
    text_transformed = cv.transform([text])
    prediction = model.predict(text_transformed)
    return prediction[0]

# Streamlit app
def main():
    st.title("Movie Reviews Sentiment Analysis App")
    st.write("I hate the movie:")

    # User input
    user_input = st.text_area("I love the movie", "")

    if st.button("Predict Sentiment"):
        if user_input:
            sentiment = predict_sentiment(user_input)
            st.write(f"The predicted sentiment is: {'Positive' if sentiment == 1 else 'Negative'}")
        else:
            st.write('I love the movie.')

if __name__ == "__main__":
    main()
