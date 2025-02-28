#1. Support Vector Machine (Classificatore)
from sklearn.datasets import load_diabetes, load_wine
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

wine = load_wine()
X = wine.data
y = wine.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definire il modello SVM con kernel lineare
model = SVC(kernel='linear')
# Addestrare il modello
model.fit(X_train, y_train)


# 2. Random Forest (Classificatore o Regressore)
from sklearn.ensemble import RandomForestClassifier

# Definire il modello Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
# Addestrare il modello
model.fit(X_train, y_train)


# 3. Regressione Logistica
from sklearn.linear_model import LogisticRegression

# Definire il modello di Regressione Logistica
model = LogisticRegression(max_iter=100)
# Addestrare il modello
model.fit(X_train, y_train)


# 4. K-Means Clustering
from sklearn.cluster import KMeans

# Definire il modello K-Means
model = KMeans(n_clusters=3, random_state=42)
# Addestrare il modello (per clustering non supervisionato non si usa y)
model.fit(X)
# Ottenere le etichette dei cluster
labels = model.labels_