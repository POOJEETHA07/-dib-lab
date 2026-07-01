import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df = pd.read_excel(r'C:\Users\student\Desktop\DS\Book2.xlsx')
print(df.head())
p = df[['Register Number', 'Mark']].values
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(p)
y_kmeans = kmeans.labels_
centers = kmeans.cluster_centers_
plt.figure(figsize=(8, 6))
plt.scatter(p[:, 0], p[:, 1], c=y_kmeans, s=50)
plt.scatter(centers[:, 0], centers[:, 1], marker='X', s=200)
plt.xlabel('Register Number')
plt.ylabel('Mark')
plt.title('K-Means Clustering')
plt.show()