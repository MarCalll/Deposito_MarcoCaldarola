import pandas as pd
from sklearn.datasets import load_wine
import seaborn as sns
import matplotlib.pyplot as plt

#Branch1
pinguini = sns.load_dataset('penguins')
print(pinguini)
pinguini.dropna(inplace=True)
print(pinguini.info())
# print(pinguini.describe())

specieCount = pinguini['species'].value_counts()
print("\nQuantità specie:\n",specieCount)

#Branch2
# studiare la relazione tra peso corporeo dei pinguini con altre variabili come sesso e lunghezza del becco
mean_body_mass_g_sex = pinguini.groupby('sex')['body_mass_g'].mean()
flipper_length_mm_sex = pinguini.groupby('sex')['flipper_length_mm'].mean()
islandCount = pinguini['island'].value_counts()
print("\nbody mass by sex:\n",mean_body_mass_g_sex)
print("\nflipper length by sex:\n",flipper_length_mm_sex)
print("\nisland count:\n",islandCount)

#Branch3
correlation_matrix = pinguini.select_dtypes(include=["number"]).corr()
correlation_matrix
plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='body_mass_g', y='flipper_length_mm', hue='species', data=pinguini, palette='Set2')
plt.title('Relazione tra peso corporeo e lunghezza delle pinne dei pinguini')
plt.xlabel('Peso corporeo (g)')
plt.ylabel('Lunghezza pinne (mm)')
plt.legend(title='Specie')
plt.show()






