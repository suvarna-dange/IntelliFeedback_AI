def get_sentiment_counts(data):
    return data['sentiment'].value_counts()

def get_sentiment_percentage(data):
    return data['sentiment'].value_counts(normalize=True) * 100

def get_total_feedback(data):
    return len(data)