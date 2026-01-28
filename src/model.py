from sklearn.cluster import KMeans
import pickle

def train_kmeans(X, k=5):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    return model

def save_model(model, path):
    with open(path, 'wb') as f:
        pickle.dump(model, f)
