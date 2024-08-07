import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize.toktok import ToktokTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pickle

# Initialize the CountVectorizer
cv = CountVectorizer()


# Save the trained vectorizer to a file
pickle.dump(cv, open('cv-vectorizer.pkl', 'wb'))



# Download necessary NLTK data
nltk.download('stopwords')

# Function to remove HTML tags and noise from text
def noiseremoval_text(text):
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text()
    text = re.sub(r'\[[^]]*\]', '', text)
    return text

# Function to tokenize text
tokenizer = ToktokTokenizer()
stopword_list = stopwords.words('english')

# Function to preprocess text
def preprocess_text(text):
    text = noiseremoval_text(text)
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    tokens = [token for token in tokens if token not in stopword_list]
    return ' '.join(tokens)

# Load dataset
@st.cache_data
def load_data():
    data=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IMDB Dataset.csv')
    data['review'] = data['review'].apply(preprocess_text)
    return data

# Train a model (simplified for demonstration)
@st.cache_data
def train_model(data):
    tfidf = TfidfVectorizer(max_features=5000)
    X = tfidf.fit_transform(data['review'])
    y = data['sentiment'].apply(lambda x: 1 if x == 'positive' else 0)

    model = LogisticRegression()
    model.fit(X, y)

    
# Save the CountVectorizer and the model
pickle.dump(cv, open('cv-vectorizer.pkl', 'wb'))
pickle.dump(mnb, open('Movie_Reviews_Sentiment_Analysis.pkl', 'wb'))


# Load the CountVectorizer and model from pickle files
save_cv = pickle.load(open('cv-vectorizer.pkl', 'rb'))
model = pickle.load(open('Movie_Reviews_Sentiment_Analysis.pkl', 'rb'))


# Streamlit app
st.title("Movie Reviews Sentiment Analysis")

# Sidebar options
option = st.sidebar.selectbox(
    "Choose a functionality",
    ["Show Data", "Train Model", "Predict Sentiment"]
)

if option == "Show Data":
    st.subheader("Dataset")
    data = load_data()
    st.write(data.head())

elif option == "Train Model":
    st.subheader("Train the Model")
    data = load_data()
    model, tfidf = train_model(data)
    st.success("Model trained and saved successfully!")

elif option == "Predict Sentiment":
    st.subheader("Predict Sentiment of a Review")
    model, tfidf = load_model()
    user_input = st.text_area("Enter a movie review:")
    if st.button("Predict"):
        if user_input:
            preprocessed_text = preprocess_text(user_input)
            X_input = tfidf.transform([preprocessed_text])
            prediction = model.predict(X_input)[0]
            sentiment = "Positive" if prediction == 1 else "Negative"
            st.write(f"Sentiment: {sentiment}")
        else:
            st.write("Please enter a review to predict.")

if __name__ == "__main__":
    st.run()
