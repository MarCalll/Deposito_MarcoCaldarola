import pandas as pd
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.decomposition import PCA

iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
X = iris.data
y = iris.target
print(df.head())
print(X)
print(y)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f"Training set: {len(X_train)} campioni")
print(f"Test set: {len(X_test)} campioni")

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
print("Matrice di confusione:\n", cm)

# Visualizza la matrice graficamente
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(cmap='Blues')
plt.show()

param_grid = {'max_depth':[3,5,7], 'criterion':['gini','entropy']}
grid_search = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5)
grid_search.fit(X_train,y_train)
print(f"Migliori parametri: {grid_search.best_params_}")

#________________________________________________________________________________________________________________________________________________________________________________________________
# 1. Creiamo un dataset di esempio
# Supponiamo di avere 200 campioni e 5 feature
np.random.seed(42)
X = np.random.rand(200, 5)
print(X)

# 2. Normalizzazione delle feature (opzionale ma spesso consigliata)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)

# 3. Istanzia PCA
# n_components = 2 significa che vogliamo ridurre i dati a 2 componenti principali
pca = PCA(n_components=2)

# 4. Eseguiamo PCA
X_pca = pca.fit_transform(X_scaled)

# 5. Possiamo stampare la varianza spiegata da ogni componente
print("Varianza spiegata da ciascuna componente:", pca.explained_variance_ratio_)

# 6. Visualizzazione dei dati su 2 componenti principali
plt.figure(figsize=(8,6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue', edgecolor='k', alpha=0.7)
plt.xlabel("Prima componente principale")
plt.ylabel("Seconda componente principale")
plt.title("Visualizzazione dati dopo PCA (2D)")
plt.show()