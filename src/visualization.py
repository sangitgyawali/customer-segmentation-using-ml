import matplotlib.pyplot as plt

def elbow_method(X):
    wcss = []
    for i in range(1, 11):
        from sklearn.cluster import KMeans
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1, 11), wcss)
    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow Method")
    plt.show()

def plot_clusters(X, labels):
    plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=labels)
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.title("Customer Segments")
    plt.show()
