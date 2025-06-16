from flask import Flask, request, jsonify, render_template
import pandas as pd
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import stopwords

app = Flask(__name__)

#nltk.download('stopwords')         #one time download and comment out after that
stop_words = set(stopwords.words('english'))

df = pd.read_csv(
    'D:\Spam-Detection-Using-Naive-Bayes\sms.tsv',
    sep='\t', names=['label', 'message']
)

def preprocess(msg):
    msg = msg.lower()
    msg = ''.join([ch for ch in msg if ch not in string.punctuation])
    words = msg.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

df['cleaned'] = df['message'].apply(preprocess)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['cleaned'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
accuracy_percent = round(accuracy * 100, 2)



@app.route("/")
def home():
    return render_template("index.html",accuracy=accuracy_percent)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_msg = data.get("message", "")
    if not input_msg.strip():
        return jsonify({"error": "Message cannot be empty"}), 400

    cleaned_msg = preprocess(input_msg)
    vectorized_msg = vectorizer.transform([cleaned_msg])
    prediction = model.predict(vectorized_msg)[0]

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
