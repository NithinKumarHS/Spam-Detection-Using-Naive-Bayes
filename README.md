# 📧 Spam Detection using Naive Bayes

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/scikit--learn-1.0+-orange" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Flask-2.0-lightgrey" alt="Flask">
</div>

A machine learning project that detects spam messages using both **Gaussian Naive Bayes** and **Multinomial Naive Bayes** classifiers. Built with Python and scikit-learn, the project includes a Flask-based web interface for interactive predictions.

## 🧠 Project Overview

This project focuses on detecting spam SMS messages using Natural Language Processing and Naive Bayes classifiers. It explores and compares the performance of both **GaussianNB** and **MultinomialNB** models.

- **Dataset**: SMS Spam Collection Dataset (`sms.tsv`)
- **Text Vectorization**: CountVectorizer
- **Algorithms**: GaussianNB and MultinomialNB
- **Interface**: Web form built using Flask and HTML/CSS
- **Accuracy**: Up to **97.43%** (MultinomialNB) and **89.89%** (GaussianNB)

## Table of Contents
- [Project Overview](#-project-overview)
- [Project Structure](#-project-structure)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Evaluation](#-model-evaluation)
- [How It Works](#-how-it-works)
- [Technologies Used](#-technologies-used)
- [Screenshots](#-screenshots)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

## 📁 Project Structure

```text
Spam-Detection-Using-Naive-Bayes/
├── SnapShots/
│   ├── Ham Snapshot.png              # Ham prediction example
│   └── Spam Snapshot.png             # Spam prediction example
├── GaussianNB_Model/                 # GaussianNB_Model
│   ├── templates/
│   │   └── index.html                # Web UI
│   ├── app.py                        # Flask application
├── MultinomialNB_Model/              # MultinomialNB_Model
│   ├── templates/
│   │   └── index.html                # Web UI
│   ├── app.py                        # Flask application
├── requirements.txt                  # Dependencies
└── sms.tsv                           # Dataset
```

## 🚀 Features

- Preprocessing and feature extraction using CountVectorizer
- Training with both GaussianNB and MultinomialNB
- Evaluation of accuracy and confusion matrix
- Web app with user-friendly interface
- Model persistence using pickle

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/NithinKumarHS/Spam-Detection-Using-Naive-Bayes.git
cd Spam-Detection-Using-Naive-Bayes
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run either implementation:
```bash
# For MultinomialNB
cd MultinomialNB_Model
python app.py

# For GaussianNB
cd GaussianNB_Model
python app.py
```

Access the web interface at:  
🌐 `http://127.0.0.1:5000`

## 📊 Model Evaluation

| Model          | Accuracy | Precision | Recall | F1-Score |
|----------------|----------|-----------|--------|----------|
| MultinomialNB  | 97.43%    | 0.97      | 0.94   | 0.95     |
| GaussianNB     | 89.89%    | 0.95      | 0.92   | 0.93     |

## 🧪 How It Works

1. User enters a message into the web form
2. The message is preprocessed and vectorized
3. The trained Naive Bayes model makes prediction
4. Result displayed as either "Spam" or "Ham"

## 🔧 Technologies Used

- Python 3.8+
- scikit-learn
- Flask
- pandas
- NLTK
- HTML/CSS

## 📸 Screenshots

<div>
  <p><b>1. Spam Result</p>
  <div align="center">
    <img src="SnapShots/Spam Snapshot.jpg" alt="Spam Prediction" width="400">
  </div>
  <p><b>2. Ham Result</p>
  <div align="center">
    <img src="SnapShots/Ham Snapshot.jpg" alt="Ham Prediction" width="400">
  </div>
</div>

## 🔮 Future Enhancements

- Add TF-IDF vectorization option
- Deploy as web service
- Improve UI with modern styling
- Add model comparison dashboard

## 👤 Author

**Nithin Kumar HS**  
GitHub: [@NithinKumarHS](https://github.com/NithinKumarHS)  
