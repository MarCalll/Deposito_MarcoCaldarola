from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

wine = load_wine()

df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
X = wine.data
y = wine.target
print(df.head())
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f"Training set: {len(X_train)} campioni")
print(f"Test set: {len(X_test)} campioni")

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

modelDecisionTree = DecisionTreeClassifier(max_depth=3, random_state=42)
modelDecisionTree.fit(X_train_scaled, y_train)

y_pred = modelDecisionTree.predict(X_test_scaled)

print(classification_report(y_test, y_pred, target_names=wine.target_names))

conf_matrix = confusion_matrix(y_test, y_pred)

# Visualizza la matrice di confusione
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=wine.target_names,
            yticklabels=wine.target_names)
plt.xlabel('Classe Predetta')
plt.ylabel('Classe Reale')
plt.title('Matrice di Confusione')
plt.show()