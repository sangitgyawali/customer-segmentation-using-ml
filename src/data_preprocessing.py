import pandas as pd

def load_and_preprocess(path):
    data = pd.read_csv(path)

    # Select useful features
    X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

    return X, data
