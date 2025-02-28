from sklearn.datasets import load_wine
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

wine = load_wine()
X = wine.data
y = wine.target
# Dividi i dati in due set: l'80% per il training e il 20% per il test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


pipeline = Pipeline([
    ('scaler',StandardScaler()),
    ('svc', SVC(kernel='rbf',C=1))
])

pipeline.fit(X_train,y_train)
y_pred = pipeline.predict(X_test)