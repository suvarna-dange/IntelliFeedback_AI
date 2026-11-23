from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_model(data):
    vectorizer = CountVectorizer()

    X = vectorizer.fit_transform(data['feedback'])
    y = data['sentiment']

    model = MultinomialNB()
    model.fit(X, y)

    return model, vectorizer