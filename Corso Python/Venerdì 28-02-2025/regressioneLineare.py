from matplotlib import pyplot as plt
import numpy as np
from sklearn.discriminant_analysis import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes, load_wine
from sklearn.metrics import mean_squared_error

# Caricamento del dataset
wine = load_diabetes()
X = wine.data
y = wine.target

# Suddivisione dei dati in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Creazione del modello di regressione lineare
model = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=None)

# Addestramento del modello
model.fit(X_train, y_train)

# Predizione sui dati di test
y_pred = model.predict(X_test)

# Calcolo dell'errore quadratico medio
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Stampa dei coefficienti
print("Coefficienti:", model.coef_)
print("Intercetta:", model.intercept_)

# Estrazione dei coefficienti e dell'intercetta
intercept = model.intercept_
coefficients = model.coef_



import matplotlib.pyplot as plt
import numpy as np

# Scegliamo una singola variabile (ad esempio la prima caratteristica)
X_single_feature = X[:, 0].reshape(-1, 1)  # prima colonna di X (ad esempio, la prima caratteristica)

# Creiamo una versione di X dove tutte le altre caratteristiche sono fissate
# (ad esempio, mettiamo tutte le altre variabili a zero per visualizzare solo l'effetto della prima)
X_modified = np.zeros_like(X)

# Manteniamo solo la prima colonna non modificata, le altre sono settate a zero
X_modified[:, 0] = X_single_feature.flatten()

# Predizione per la variabile modificata
y_pred = model.predict(X_modified)

# Creiamo il grafico scatter
plt.figure(figsize=(8, 6))
plt.scatter(X_single_feature, y, color='blue', label='Dati reali', alpha=0.5)

# Tracciamo la retta di regressione che mostra l'intercetta
plt.plot(X_single_feature, y_pred, color='red', label='Regr. Lineare', linewidth=2)

# Aggiungiamo il titolo e le etichette
plt.xlabel('Caratteristica 1 (ad esempio, alcol)')
plt.ylabel('Target')
plt.title('Scatter Plot con la Curva di Regressione Lineare e Intercetta')
plt.legend()
plt.grid(True)

# Mostriamo il grafico
plt.show()

