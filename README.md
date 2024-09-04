# Sentiment-Analysis-Project
Sentiment Analysis also known as opinion mining helps to classify ideas and opinions as positive, negative, or neutral and determines emotions whether sad or happy.
This project focuses on performing sentiment analysis on text data. The goal is to build a model that can classify text data into different categories such as positive, negative, or neutral reviews.

# Dataset
IMDB movie reviews dataset, sourced from Kaggle, was used for this project. The dataset contains 50,000 movie reviews.

# Data preprocessing 
Text Normalization 
* Lowering text. 
* Tokenization .
* Stemming. 
* Removing stopwords.
* Removing punctuation.
  
Vectorization

This is the process of converting text into numerical vectors.  For this project, Term Frequency-Inverse Document Frequency (TF-IDF) and Bag of Words (BoW ) were used.

# Model Training
Naive Bayes was used in this project. The model was trained using both Bag of Words (BoW) and Term Frequency-Inverse Document Frequency (TF-IDF) representations. The Naive Bayes classifier is used to classify reviews into positive or negative categories based on the features extracted from BoW and TF-IDF.

# Model Evaluation
The classification report and accuracy of the Naive Bayes model includes:

Accuracy: 0.8517, meaning the model predicted the sentiment correctly for approximately 85% of the text samples.

Classification Report:
* Precision: 0.85
* Recall: 0.85
* F1-score: 0.85


