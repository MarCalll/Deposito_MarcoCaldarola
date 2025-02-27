from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

wine = load_wine()
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
X = wine.data
y = wine.target
# Dividi i dati in due set: l'80% per il training e il 20% per il test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Visualizza il numero di campioni per ciascuna classe e calcola le statistiche di base delle feature
countClassi=pd.Series(y).value_counts()
print(df.info())
print(countClassi)

# Visualizzazione: crea un grafico a barre per mostrare la distribuzione delle classi.
class_names = wine.target_names
plt.figure(figsize=(8, 6))
sns.barplot(x=class_names, y=countClassi)
plt.title('Wine Dataset')
plt.xlabel('Nomi classi')
plt.ylabel('Quantità')
plt.show()

# Applica la PCA (Principal Component Analysis) per ridurre le dimensioni delle feature a 2 componenti principali
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualizzazione: crea un grafico scatter 2D per rappresentare i dati trasformati, con i punti colorati in base alla classe
plt.figure(figsize=(8,6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue', edgecolor='k', alpha=0.7)
plt.xlabel("Prima componente principale")
plt.ylabel("Seconda componente principale")
plt.title("Visualizzazione dati dopo PCA (2D)")
plt.show()

# Utilizza un modello RandomForestClassifier per la classificazione.
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)
print("Classification Report:")
# Valuta le prestazioni utilizzando le metriche di accuratezza, precisione, recall e F1-score.
print(classification_report(y_test, y_pred))

# Visualizza le feature più importanti del dataset Wine secondo il modello Random Forest, utilizzando un grafico a barre
feature_importances = rf_model.feature_importances_
importance_df = pd.DataFrame({
    'Feature': wine.feature_names,
    'Importance': feature_importances
})

importance_df = importance_df.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df)
plt.title('Importanza delle Feature nel modello RandomForest')
plt.xlabel('Importanza')
plt.ylabel('Feature')
plt.show()

# Genera e visualizza la matrice di confusione per valutare la qualità della classificazione.
conf_matrix = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=wine.target_names)
disp.plot(cmap='Blues')
plt.show()

# Utilizza la GridSearchCV per ottimizzare i parametri del Random Forest (ad esempio: numero di estimatori e profondità massima dell'albero)
param_grid = {
    'max_depth': [3, 5, 7],                # Profondità massima dell'albero
    'criterion': ['gini', 'entropy'],      # Criterio di divisione
    'n_estimators': [50, 100, 200]         # Numero di alberi nella foresta
}
grid_search = GridSearchCV(rf_model, param_grid, cv=5)
grid_search.fit(X_train, y_train)
print("Migliori parametri trovati:", grid_search.best_params_)

