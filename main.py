from src.data_preprocessing import load_and_preprocess
from src.model import train_kmeans, save_model
from src.visualization import elbow_method, plot_clusters

# Load data
X, data = load_and_preprocess("data/mall_customers.csv")

# Find best K
elbow_method(X)

# Train model
model = train_kmeans(X, k=5)

# Predict clusters
data['Cluster'] = model.predict(X)

# Plot result
plot_clusters(X, data['Cluster'])

# Save model
save_model(model, "models/kmeans_model.pkl")

print("Customer Segmentation Completed Successfully!")
