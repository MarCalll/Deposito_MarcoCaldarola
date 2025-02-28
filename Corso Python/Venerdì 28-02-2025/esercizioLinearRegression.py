from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.discriminant_analysis import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


dataset = load_diabetes()
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
X = dataset.data
y = dataset.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=None)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
y_pred_scaled = model.predict(X_test_scaled)

#l'errore quadratico medio tra i dati di train e i test e dice quanto in media sbaglia la previsione
mse = mean_squared_error(y_test, y_pred)
mse_scaled = mean_squared_error(y_test, y_pred_scaled)

# Il coefficiente di determinazione (R2R2) è una misura che ci dice quanto bene un modello predice i dati
# Un R2=0.4526R2=0.4526 significa che il modello è in grado di spiegare circa il 45.26% della variabilità nei dati di test.
# In altre parole, il modello riesce a fare previsioni corrette per circa il 45% dei dati.
r2 = r2_score(y_test, y_pred)
r2_scaled = r2_score(y_test, y_pred_scaled)

plt.bar(['MSE', 'R^2'], [mse, r2])
plt.ylabel('Valori')
plt.title('Prestazioni del modello sui dati di test')
plt.show()

print(f"Errore Quadratico Medio (MSE): {mse}")
print(f"Coefficiente di Determinazione (R^2): {r2}")

print(f"Errore Quadratico Medio (MSE): {mse_scaled}")
print(f"Coefficiente di Determinazione (R^2): {r2_scaled}")

from sklearn.linear_model import LinearRegression

# Crea e allena il modello
model = LinearRegression()
model.fit(X_train, y_train)

# Ottieni l'intercetta
intercept = model.intercept_
# Visualizza l'intercetta
print(f"L'intercetta del modello è: {intercept}")


