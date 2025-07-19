import streamlit as st
import pickle as pkl
import string
import nltk
from nltk import PorterStemmer
from nltk.corpus import stopwords

tf = pkl.load(open('vectorizer.pkl','rb'))
model = pkl.load(open('model.pkl','rb'))

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

st.title('Email/SMS Spam Classifier')

input_sms = st.text_area('Enter the message')

if st.button('Predict'):

    transformed_sms = transform_text(input_sms)

    vectorized_sms = tf.transform([transformed_sms])

    prediction = model.predict(vectorized_sms)[0]

    if prediction == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')