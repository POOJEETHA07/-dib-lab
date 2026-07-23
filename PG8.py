from sklearn import preprocessing 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier, plot_tree 
import matplotlib.pyplot as plt 
data = [ 
    ['sunny', 85, 'high', False, 'no'], 
    ['sunny', 80, 'normal', True, 'no'], 
    ['overcast', 83, 'high', False, 'yes'], 
    ['rainy', 70, 'high', False, 'yes'], 
    ['rainy', 68, 'normal', False, 'yes'], 
    ['rainy', 65, 'normal', True, 'no'], 
    ['overcast', 64, 'high', True, 'yes'], 
    ['sunny', 72, 'high', False, 'no'], 
    ['sunny', 69, 'high', True, 'yes'], 
    ['rainy', 75, 'high', True, 'no'], 
    ['sunny', 75, 'normal', False, 'yes'], 
    ['overcast', 72, 'normal', True, 'yes'], 
    ['overcast', 81, 'high', False, 'yes'], 
    ['rainy', 71, 'normal', True, 'no'] 
] 
le = preprocessing.LabelEncoder() 
X = [] 
for entry in data: 
    X.append([le.fit_transform([entry[0]])[0], entry[1], le.fit_transform([entry[2]])[0], 
entry[3]]) 
y = [entry[4] for entry in data] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
random_state=42) 
clf = DecisionTreeClassifier(random_state=42) 
clf.fit(X_train, y_train)
plt.figure(figsize=(10, 6)) 
plot_tree(clf, filled=True, feature_names=['Outlook', 'Temperature', 'Humidity', 
'Windy']) 
plt.title("Decision Tree Visualization - Golf Dataset") 
plt.show() 
y_pred = clf.predict(X_test) 
accuracy = sum(y_pred == y_test) / len(y_test) 
print(f"Accuracy on test set: {accuracy:.2f}")