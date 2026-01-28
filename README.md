# Customer Segmentation using Machine Learning
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white) ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0.24.2-green?logo=scikitlearn) ![License](https://img.shields.io/badge/License-MIT-yellow)

Customer Segmentation is a critical task in business analytics to **group customers based on similar characteristics** such as income and spending behavior. This project uses **K-Means Clustering** in Python to segment customers and provide actionable insights for marketing strategies.

**Dataset:** [Mall Customer Segmentation Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) from Kaggle. Features: CustomerID, Age, Gender, Annual Income (k$), Spending Score (1-100).

**Tools & Technologies:** Python 3.x, Pandas, NumPy, Scikit-learn (KMeans), Matplotlib / Seaborn, VS Code / Jupyter Notebook.

**Installation:**  
```bash
git clone https://github.com/sangitgyawali/customer-segmentation-using-ml.git
cd customer-segmentation-using-ml
pip install -r requirements.txt
````
How to Run:
````
python main.py
````
This loads and preprocesses the dataset, trains K-Means clustering, predicts customer clusters, visualizes clusters, and saves the trained model in models/kmeans_model.pkl.

This loads and preprocesses the dataset, trains K-Means clustering, predicts customer clusters, visualizes clusters, and saves the trained model in models/kmeans_model.pkl.

Results: Customers are segmented into 5 clusters: Low Income – Low Spending, Low Income – High Spending, High Income – Low Spending, High Income – High Spending, Average Customers. Cluster visualizations are saved in outputs/cluster_plots.png.

Business Insights: Target high-value customers for premium offers, identify low-spending groups for promotions, and optimize marketing campaigns.

Future Scope: Include more features (Age, Gender, location, purchase history), test DBSCAN or Hierarchical Clustering, create a web app with Streamlit/Flask, integrate with e-commerce platforms.
