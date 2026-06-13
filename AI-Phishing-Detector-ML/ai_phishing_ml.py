import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

print("================================")
print("      AI PHISHING DETECTOR")
print("================================")

data = {
    "text": [
        "secure bank login update account",
        "verify your password immediately",
        "free gift click now",
        "meeting scheduled tomorrow",
        "project report attached",
        "team discussion at 5 pm",
        "bank account suspended verify now",
        "claim free reward now"
    ],
    "label": [
        "Phishing",
        "Phishing",
        "Phishing",
        "Safe",
        "Safe",
        "Safe",
        "Phishing",
        "Phishing"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

model = MultinomialNB()
model.fit(X, df["label"])

message = input("\nEnter URL or Message: ")

message_vector = vectorizer.transform([message])

prediction = model.predict(message_vector)

print("\nAI Phishing Analysis")
print("---------------------")
print("Input:", message)
print("Prediction:", prediction[0])