import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
x = [4, 5, 10, 4, 3, 11, 14, 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [0, 1, 1, 0, 0, 1, 1, 0, 1, 1]
data = list(zip(x, y))
print("Data Points:", data)
new_x = 8
new_y = 21
new_point = [(new_x, new_y)]
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data, classes)
prediction = knn.predict(new_point)
print("Prediction for k=1:", prediction)
plt.figure(figsize=(6, 5))
plt.scatter(x + [new_x], y + [new_y],
            c=classes + [prediction[0]], s=100)
plt.text(
    x=new_x - 1.7,
    y=new_y - 0.7,
    s=f"New Point, Class: {prediction[0]}"
)
plt.title("KNN Classification (k=1)")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(data, classes)
prediction = knn.predict(new_point)
print("Prediction for k=5:", prediction)
plt.figure(figsize=(6, 5))
plt.scatter(x + [new_x], y + [new_y],
            c=classes + [prediction[0]], s=100)
plt.text(
    x=new_x - 1.7,
    y=new_y - 0.7,
    s=f"New Point, Class: {prediction[0]}"
)
plt.title("KNN Classification (k=5)")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()