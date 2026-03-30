import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = {
    'message': [
        'Win money now!!!',
        'Hey bro how are you?',
        'Free entry in 2 lakh prize',
        'Let’s meet tomorrow',
        'Claim your free reward now',
        'Are you coming to class?'
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}

df = pd.DataFrame(data)
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])
y = df['label_num']


model = MultinomialNB()
model.fit(X, y)


def predict_spam(message):
    msg = vectorizer.transform([message])
    result = model.predict(msg)
    return "SPAM" if result[0] == 1 else "NOT SPAM"