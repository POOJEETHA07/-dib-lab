import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv(r"C:\Users\student\Desktop\DS\student_dataset.csv")
df['Name'] = LabelEncoder().fit_transform(df['Name'])
print(df.head())
X_train, X_test, y_train, y_test = train_test_split(
    df[['Registerno', 'Name', 'Marks']], df['Result'], test_size=0.3, random_state=0
)

scaler = StandardScaler()
X_train, X_test = scaler.fit_transform(X_train), scaler.transform(X_test)

model = LogisticRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))