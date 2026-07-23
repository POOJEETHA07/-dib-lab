from sklearn.naive_bayes import CategoricalNB
import numpy as np 
x = np.array([
    [0,0,0,0],
    [0,0,0,1],
    [1,0,0,0],
    [2,1,0,0],
    [2,2,1,0],
    [2,2,1,1],
    [1,2,1,1],
    [0,1,0,0],
    [0,2,1,0],
    [2,1,1,0],
    [0,1,1,1],
    [1,1,0,1],
    [1,0,1,0],
    [2,1,0,1]
])
y = np.array([0,0,1,1,1,0,1,0,1,1,1,1,1,0])
clf = CategoricalNB()
clf.fit(x,y)
X_test = np.array([[1,2,1,1]])
predicted = clf.predict(X_test)
if predicted[0] == 1:
    print("Prediction:Play Golf")
else:
    print("Prediction:Don't Play Golf")   
    
             