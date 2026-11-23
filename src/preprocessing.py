import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)

    data['sentiment'] = data['sentiment'].str.strip()
    data['feedback'] = data['feedback'].str.lower()

    return data