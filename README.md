# 📩 SMS/Email Spam Classifier

🚀 [**Live Demo**]([https://your-render-app-url.onrender.com](https://email-sms-spam-classifier-o6ot.onrender.com/)) – Click to try it out!

---

## 📚 Overview

This is an end-to-end **SMS/Email Spam Classifier** built using classical **Machine Learning** and **NLP** techniques. It classifies messages as **Spam** or **Not Spam** based on their content using a pre-trained **Logistic Regression** model.

The project includes:

- Data cleaning & preprocessing
- Feature extraction using **TF-IDF**
- Custom text transformation (tokenization, stopword removal, stemming)
- Model building & evaluation
- A web interface using **Streamlit**
- Deployment on **Render**

---

## 📈 Dataset

The dataset used is the classic **SMS Spam Collection**, consisting of labeled SMS messages classified as either "spam" or "ham".

- Total messages: 5,572  
- Spam: ~13%  
- Ham: ~87%

---

## 🔍 Text Preprocessing

The following steps are applied before vectorization:

- Lowercasing  
- Removing punctuation & special characters  
- Removing stopwords  
- Stemming (Porter Stemmer)  
- Tokenization  

Custom function used:
```python
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    text = [word for word in text if word.isalnum()]
    text = [word for word in text if word not in stopwords.words('english') and word not in string.punctuation]
    text = [ps.stem(word) for word in text]
    return " ".join(text)
```

---

## 🧠 Model Details & 🌐 Live App Usage

### 🧠 Model Details

- **Vectorizer:** TF-IDF with `max_features=3000`  
- **Classifier:** Logistic Regression (achieves ~96% accuracy)  
- **Serialization:** Model, vectorizer, and transform function saved using Pickle

### 🌐 How to Use the Live App

1. Visit: [https://your-render-app-url.onrender.com](https://your-render-app-url.onrender.com)  
2. Type or paste a message into the input box  
3. Click **Predict**  
4. The app will classify it as **Spam** or **Not Spam**

---

## 📂 Project Structure

```
📁 sms-spam-classifier/
├── App.py                 # Streamlit frontend
├── model.pkl              # Trained Logistic Regression model
├── vectorizer.pkl         # TF-IDF vectorizer
├── transform_text.pkl     # Preprocessing function
├── requirements.txt       # Minimal dependencies
└── README.md              # Project documentation
```

---

## 🛠️ Local Setup

```bash
git clone https://github.com/your-username/sms-spam-classifier.git
cd sms-spam-classifier
pip install -r requirements.txt
streamlit run App.py
```

---

## ✅ Requirements

Only minimal packages used:
```txt
streamlit
scikit-learn
pandas
nltk
```

---

## 🚀 Deployment

The app is deployed on [Render](https://render.com) using:
- GitHub repo integration
- A `requirements.txt` for dependency management
- `App.py` as the entry point

---

## ✨ Credits

- Dataset: [UCI SMS Spam Collection](https://www.dt.fee.unicamp.br/~tiago/smsspamcollection/)  
- Developed by: **Uday Kumar**

---

## 📬 Contact

- 📧 [LinkedIn](https://www.linkedin.com/in/your-linkedin)
- 🌐 [Portfolio](https://your-portfolio-link.com)

---

⭐ If you like this project, don't forget to star ⭐ the repo!
