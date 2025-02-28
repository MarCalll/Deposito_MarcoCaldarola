from matplotlib import pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.metrics import adjusted_rand_score, homogeneity_score


dataset = load_iris()
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
X = dataset.data
y = dataset.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(df)

kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
kmeans.fit(X_train) 

y_kmeans = kmeans.predict(X)

# Visualizza i cluster (usando due caratteristiche)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis', edgecolor='k', s=100, alpha=0.7)

# Mostra i centroidi in rosso
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='red', marker='X', s=300, label='Centroidi')

plt.title('Cluster K-Means sul dataset Iris')
plt.xlabel('Lunghezza Sepalo (cm)')
plt.ylabel('Larghezza Sepalo (cm)')
plt.legend()
plt.show()

# 1. Calcola la matrice di confusione
cm = confusion_matrix(y, y_kmeans)

# 2. Visualizza la matrice di confusione
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Cluster 0', 'Cluster 1', 'Cluster 2'], yticklabels=dataset.target_names)
plt.title('Confronto tra Cluster e Specie Reali')
plt.xlabel('Cluster Assegnati da K-Means')
plt.ylabel('Etichette Reali (Specie Iris)')
plt.show()

# Calcola l'Adjusted Rand Index (ARI)
ari = adjusted_rand_score(y, y_kmeans)

# Calcola l'Homogeneity Score
homogeneity = homogeneity_score(y, y_kmeans)

# Stampa i risultati
print(f"Adjusted Rand Index (ARI): {ari:.2f}")
print(f"Homogeneity Score: {homogeneity:.2f}")
