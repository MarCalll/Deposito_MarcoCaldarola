import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Percorso del file CSV
file_path = 'train.csv'

# Caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)

#le prime righe del DataFrame per confermare 
df.head()


#-------------


df.tail()


#-------------


df.info()


#-------------


df.describe()


#-------------


df.shape


#-------------


df.info()


#-------------


df.columns


#-------------


df.index


#-------------


age = df["Age"] #selezione singola colonna
age


#-------------


selection = df[["Age", "Survived", "Fare"]] #selezione delle colonne
selection


#-------------


print(df.iloc[1:7]) #selezione sulle righe


#-------------


survivors = df[df['Survived']==1] #selezione condizionata
survivors


#-------------


aged = df[df["Age"] > 50]
aged


#-------------


sorted_aged = aged.sort_values('Age',ascending=True)
sorted_aged


#-------------


df.isnull().sum()


#-------------


df = df.drop('Cabin', axis=1)
df


#-------------


df_notnull = df.dropna()
df_notnull.isnull().sum()


#-------------


df['Age'] = df['Age'].fillna(df['Age'].mean())
df.isnull().sum()


#-------------


df['Embarked'].unique()


#-------------


df['Embarked'].value_counts()


#-------------


mean_age_byclass = df.groupby('Pclass')['Age'].mean()
mean_age_byclass


#-------------


df.groupby('Pclass')['Fare'].mean()


#-------------


df['AgeGroup'] = pd.cut(df['Age'], bins=range(0, 85, 5), right=False)
mean_fare_byagegroup = df.groupby('AgeGroup')['Fare'].mean()
mean_fare_byagegroup


#-------------





correlation_matrix = df.select_dtypes(include=["number"]).corr()
correlation_matrix
plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()


#-------------


df['Sex'] = df['Sex'].astype('category')
df['Sex_code'] = df['Sex'].cat.codes
df[['Sex', 'Sex_code']].head()


#-------------


correlation_matrix = df.select_dtypes(include=["number"]).corr()
correlation_matrix
plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()


#-------------


df_encoded = pd.get_dummies(df, columns=['Embarked'], prefix='Embarked')
df_encoded.head()


#-------------


correlation_matrix = df_encoded.select_dtypes(include=["number","bool"]).corr()
correlation_matrix
plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()


# Cos'è un istogramma?
# Un istogramma è un tipo di grafico utilizzato per rappresentare la distribuzione di una variabile numerica. Suddivide i dati in intervalli (o "bin") e mostra la frequenza con cui i valori rientrano in ciascun intervallo.
# 
# Quando usarlo?
# 
# Per capire la distribuzione di una variabile numerica.
# Per individuare valori anomali o outlier.
# Per confrontare distribuzioni tra diversi gruppi.

# import seaborn as sns
# 
# sns.histplot(data, bins=numero_di_intervalli, kde=True)
# plt.xlabel('Nome Variabile')
# plt.ylabel('Frequenza')
# plt.title('Titolo dell’Istogramma')
# plt.show()
# 

# bins: Numero di intervalli in cui suddividere i dati.
# edgecolor: Colore del bordo delle barre.
# alpha: Trasparenza delle barre.
# kde: Se True, aggiunge una linea di densità della distribuzione.

#-------------

plt.figure(figsize=(10, 5))
sns.histplot(df['Age'].dropna(), bins=30, kde=True, color='blue')
plt.xlabel('Età')
plt.ylabel('Frequenza')
plt.title('Distribuzione dell\'età dei passeggeri con Seaborn')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


# Grafico a Barre (Bar Plot)
# Cos'è un grafico a barre?
# Un grafico a barre è utilizzato per confrontare quantità tra diverse categorie. Le barre possono essere orizzontali o verticali e mostrano la relazione tra una variabile categoriale e una numerica.
# 
# Quando usarlo?
# 
# Per confrontare valori tra categorie discrete (es. sopravvissuti vs. non sopravvissuti).
# Per mostrare distribuzioni di dati categoriali.
# Per confrontare medie, conteggi o altre metriche.

# sns.barplot(x=categoria, y=valore, data=df, palette='Blues')
# plt.xlabel('Nome Categoria')
# plt.ylabel('Valore')
# plt.title('Titolo del Grafico a Barre')
# plt.show()
# 
# color: Cambia il colore delle barre.
# edgecolor: Bordo delle barre.
# palette: Seleziona una palette di colori in Seaborn.
# hue: Consente di suddividere i dati in sottocategorie.

#-------------


survival_counts = df['Survived'].value_counts()
survival_counts


#-------------


# Contare i passeggeri sopravvissuti e non sopravvissuti
survival_counts = df['Survived'].value_counts()

plt.figure(figsize=(8, 5))
sns.barplot(x=survival_counts.index, y=survival_counts.values, palette=['red', 'green'])
plt.xlabel('Stato di Sopravvivenza')
plt.ylabel('Numero di Passeggeri')
plt.title('Confronto tra passeggeri sopravvissuti e non sopravvissuti (Seaborn)')
plt.xticks(ticks=[0, 1], labels=['Non Sopravvissuti', 'Sopravvissuti'])
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


#-------------





# Cos'è un Box Plot?
# Un box plot (o diagramma a scatola e baffi) è un grafico utilizzato per mostrare la distribuzione di una variabile numerica e identificare eventuali outlier. Visualizza:
# 
# Mediana (linea centrale nella scatola)
# Primo e terzo quartile (bordo inferiore e superiore della scatola)
# Valori minimi e massimi (baffi)
# Outlier (punti fuori dai baffi)
# Quando usarlo?
# 
# Per confrontare distribuzioni tra diverse categorie.
# Per individuare outlier nei dati.
# Per capire la variabilità e la dispersione dei dati.

# sns.boxplot(x=categoria, y=valore, data=df, palette='Set2')
# plt.xlabel('Nome Categoria')
# plt.ylabel('Valore')
# plt.title('Titolo del Box Plot')
# plt.show()
# 
# vert=True → Box verticale (False per orizzontale).
# patch_artist=True → Rende la scatola colorata.
# palette → Seleziona una palette di colori in Seaborn.
# hue → Divide i dati in sottocategorie.

#-------------


# Creare un box plot con Seaborn per confrontare il prezzo dei biglietti tra le classi di viaggio (Pclass)
plt.figure(figsize=(8, 5))
sns.boxplot(x='Pclass', y='Fare', data=df, palette='Set2')
plt.xlabel('Classe di Viaggio')
plt.ylabel('Prezzo del Biglietto (Fare)')
plt.title('Distribuzione del prezzo del biglietto per classe di viaggio')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


# Calcolo dell'IQR (Intervallo Interquartile):
# IQR=Q3−Q1IQR = Q3 - Q1IQR=Q3−Q1
# Dove:
#     • Q1 (Primo Quartile): Il 25% dei dati è inferiore a questo valore.
#     • Q3 (Terzo Quartile): Il 75% dei dati è inferiore a questo valore.
#     • Definizione dei limiti dei baffi (whiskers):
#     • Valore minimo accettabile = Q1−1.5×IQRQ1 - 1.5 \times IQRQ1−1.5×IQR
#     • Valore massimo accettabile = Q3+1.5×IQRQ3 + 1.5 \times IQRQ3+1.5×IQR
# I baffi del box plot si estendono fino all’ultimo valore che rientra in questo intervallo.

# Violin Plot (Grafico a Violino) 
# Cos'è un Violin Plot?
# Un violin plot è una combinazione tra un box plot e un kde plot (Kernel Density Estimation). Mostra:
# 
# Distribuzione dei dati (come un istogramma o una curva di densità).
# Mediana e intervalli interquartili (come un box plot).
# Simmetria e variazione dei dati.
# Quando usarlo?
# 
# Per analizzare la distribuzione di una variabile numerica in diverse categorie.
# Per confrontare densità e forma della distribuzione tra gruppi.
# Quando un box plot non è sufficiente a mostrare dettagli sulla distribuzione.

# sns.violinplot(x=categoria, y=valore, data=df, palette='coolwarm')
# plt.xlabel('Nome Categoria')
# plt.ylabel('Valore')
# plt.title('Titolo del Violin Plot')
# plt.show()
# 
# split=True → Divide il grafico a violino tra due gruppi (es. maschi e femmine).
# palette → Seleziona una palette di colori.
# inner='quartile' → Mostra la mediana e i quartili all'interno del violino.
# hue → Divide i dati in sottogruppi.

#-------------


# Creare un violin plot per la distribuzione dell'età tra le classi di viaggio
plt.figure(figsize=(8, 5))
sns.violinplot(x='Pclass', y='Age', data=df, palette='coolwarm', inner='quartile')
plt.xlabel('Classe di Viaggio')
plt.ylabel('Età')
plt.title('Distribuzione dell\'età per classe di viaggio (Violin Plot)')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


# Scatter Plot (Grafico a Dispersione)
# Cos'è uno Scatter Plot?
# Uno scatter plot è un tipo di grafico che rappresenta i dati su un piano cartesiano, mostrando la relazione tra due variabili numeriche.
# Ogni punto nel grafico rappresenta una coppia di valori (x, y).
# 
# Quando usarlo?
# 
# Per analizzare la correlazione tra due variabili numeriche.
# Per individuare trend o pattern nei dati.
# Per rilevare outlier o anomalie nei dati.

# plt.scatter(x, y, color='blue', alpha=0.5)
# plt.xlabel('Nome Asse X')
# plt.ylabel('Nome Asse Y')
# plt.title('Titolo del Grafico a Dispersione')
# plt.show()
# 
# Parametri importanti:
# 
# alpha → Regola la trasparenza dei punti per evitare sovrapposizioni.
# hue → Colora i punti in base a una categoria.
# style → Cambia la forma dei punti in base a una categoria.

#-------------


# Creare uno scatter plot per la relazione tra età e prezzo del biglietto
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='Fare', data=df, hue='Pclass', style='Pclass', palette='coolwarm', alpha=0.7)
plt.xlabel('Età')
plt.ylabel('Prezzo del Biglietto (Fare)')
plt.title('Relazione tra Età e Prezzo del Biglietto (Scatter Plot)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# Line Plot (Grafico a Linea)
# Cos'è un Line Plot?
# Un grafico a linea è utilizzato per mostrare l'andamento di una variabile numerica rispetto a un'altra variabile numerica o temporale.
# Viene spesso usato per analizzare trend nel tempo.
# 
# Quando usarlo?
# 
# Per osservare l'andamento di una variabile numerica.
# Per identificare pattern o trend nel tempo.
# Per confrontare serie temporali o variazioni di valori.

# sns.lineplot(x=x, y=y, data=df, marker='o')
# plt.xlabel('Nome Asse X')
# plt.ylabel('Nome Asse Y')
# plt.title('Titolo del Grafico a Linea')
# plt.show()
# 
# marker='o' → Mostra i punti della serie dati.
# linestyle='-' → Linea continua.
# hue → Colora la linea in base a una categoria.

#-------------


# Creare un line plot per il prezzo medio del biglietto in base alla classe di viaggio
fare_mean_per_class = df.groupby("Age")["Fare"].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.lineplot(x='Age', y='Fare', data=fare_mean_per_class, marker='o', linestyle='dotted', color='blue')
plt.xlabel('Eta')
plt.ylabel('Prezzo Medio del Biglietto (Fare)')
plt.title('Prezzo Medio del Biglietto per Eta (Line Plot)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# Heatmap (Mappa di Calore)
# Cos'è una Heatmap?
# Una heatmap è un tipo di grafico che rappresenta una matrice di valori numerici utilizzando una scala di colori.
# Viene spesso usata per visualizzare correlazioni tra variabili o densità di dati.
# 
# Quando usarlo?
# 
# Per analizzare correlazioni tra variabili numeriche.
# Per visualizzare relazioni tra variabili in un dataset.
# Per evidenziare pattern all'interno di una matrice di dati.

# sns.heatmap(data=df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Titolo della Heatmap')
# plt.show()
# 
# data=df.corr() → Calcola la matrice di correlazione.
# annot=True → Mostra i valori numerici all'interno delle celle.
# cmap='coolwarm' → Sceglie una scala di colori.
# fmt=".2f" → Formatta i valori con due decimali.

#-------------


# Creare una heatmap della correlazione tra variabili numeriche nel Titanic dataset
plt.figure(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Mappa di Calore delle Correlazioni tra Variabili Numeriche')
plt.show()


# Pair Plot (Grafico a Coppie - Pairplot)
# Cos'è un Pair Plot?
# Un pair plot è una matrice di grafici a dispersione (scatter plot) che mostra la relazione tra tutte le variabili numeriche in un dataset.
# Include anche istogrammi sulla diagonale, che rappresentano la distribuzione di ciascuna variabile.
# 
# Quando usarlo?
# 
# Per esplorare relazioni tra variabili numeriche.
# Per identificare correlazioni, cluster o outlier.
# Per analizzare dati prima di applicare modelli di Machine Learning.

# sns.pairplot(df, hue='categoria', palette='coolwarm')
# plt.show()
# 
# hue='categoria' → Colora i punti in base a una variabile categoriale.
# palette → Seleziona una palette di colori.
# corner=True → Mostra solo metà della matrice per risparmiare spazio.

#-------------


# Creare un pair plot per analizzare le relazioni tra variabili numeriche
plt.figure(figsize=(10, 6))
sns.pairplot(df.select_dtypes(include=['number']), hue='Pclass', palette='coolwarm', corner=True)
plt.show()


# Come e perché scegliere una variabile per il parametro hue nei grafici?
# Il parametro hue in Seaborn permette di differenziare i dati in base a una variabile categoriale, assegnando colori diversi ai gruppi distinti.
# L'uso di hue aiuta a evidenziare pattern, relazioni e differenze tra le categorie.
# 
# Perché scegliere un hue?
# Utilizzare un hue appropriato può:
# 
# Aggiungere più informazioni visive → Distinguere categorie in un singolo grafico.
# Evidenziare differenze tra gruppi → Mostrare variazioni tra classi, generi, ecc.
# Migliorare la leggibilità → Riconoscere facilmente sottogruppi nei dati.
# Esempi pratici con il dataset Titanic:
# 
# Variabile (hue)	Quando sceglierla?	Esempio di utilizzo
# Pclass (Classe di viaggio)	Quando si vuole vedere la distribuzione tra le classi di viaggio	
# Survived (Sopravvissuti vs Non)	Per evidenziare le differenze tra chi è sopravvissuto e chi no	
# Sex (Genere)	Per confrontare uomini e donne	hue="Sex" 
# Embarked (Porto di imbarco)	Per vedere come i passeggeri sono distribuiti in base al porto	

# Pie Chart (Grafico a Torta) 
# Cos'è un Pie Chart?
# Un grafico a torta è un tipo di grafico utilizzato per rappresentare proporzioni di una variabile categoriale, suddividendo i dati in fette.
# Ogni fetta rappresenta una percentuale rispetto al totale.
# 
# Quando usarlo?
# 
# Per mostrare la distribuzione percentuale di una categoria.
# Quando hai un numero limitato di categorie distinte.
# Per confrontare la composizione di un gruppo rispetto al totale.
# 
# Quando NON usarlo?
# 
# Se hai troppi segmenti, il grafico diventa difficile da leggere.
# Se le differenze tra le categorie sono minime, meglio usare un bar plot.

# plt.pie(valori, labels=etichette, autopct='%1.1f%%', colors=colori, startangle=90)
# plt.title('Titolo del Grafico a Torta')
# plt.show()
# 
# labels=etichette → Nomi delle categorie.
# autopct='%1.1f%%' → Mostra le percentuali.
# colors=colori → Personalizza i colori.
# startangle=90 → Ruota il grafico per allinearlo meglio.
# explode → Separa una fetta per evidenziarla.

#-------------


# Contare i passeggeri sopravvissuti e non sopravvissuti
survival_counts = df['Survived'].value_counts()

# Creare un pie chart con Matplotlib
plt.figure(figsize=(7, 7))
plt.pie(survival_counts, labels=['Non Sopravvissuti', 'Sopravvissuti'], autopct='%1.1f%%',
        colors=['red', 'green'], startangle=90, explode=[0, 0.1])
plt.title('Distribuzione dei passeggeri sopravvissuti')
plt.show()


# Count Plot (Grafico di Conteggio) 
# Cos'è un Count Plot?
# Un count plot è un tipo di grafico a barre che mostra il conteggio delle occorrenze di ciascuna categoria di una variabile categoriale.
# A differenza di un bar plot che può rappresentare valori numerici aggregati, il count plot conta direttamente le occorrenze di ogni categoria.
# 
# Quando usarlo?
# 
# Per visualizzare la distribuzione di una variabile categoriale.
# Per contare e confrontare le categorie in un dataset.
# Per evidenziare disparità tra gruppi (es. numero di passeggeri per classe, numero di sopravvissuti per sesso, ecc.).

# sns.countplot(x=variabile_categorica, data=df, palette='coolwarm')
# plt.xlabel('Nome Categoria')
# plt.ylabel('Conteggio')
# plt.title('Titolo del Count Plot')
# plt.show()
# 
# x=variabile_categorica → La variabile che vogliamo contare.
# hue → Suddivide i dati in base a un'altra categoria (es. Sex, Survived).
# palette → Seleziona una palette di colori.

#-------------


# Creare un count plot per il numero di passeggeri per classe di viaggio suddiviso per sesso
plt.figure(figsize=(8, 5))
sns.countplot(x='Pclass', data=df, hue='Sex', palette='coolwarm')
plt.xlabel('Classe di Viaggio')
plt.ylabel('Numero di Passeggeri')
plt.title('Numero di Passeggeri per Classe di Viaggio suddiviso per Sesso (Count Plot)')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


#-------------

fig = px.scatter(df, x="Age", y="Fare", color="Pclass", size="Fare", hover_data=["Sex", "Embarked"])
fig.show()


#-------------




# Selezionare solo colonne numeriche e calcolare la matrice di correlazione
corr_matrix = df.select_dtypes(include=['number']).corr()

# Creare una heatmap interattiva con Plotly
fig = px.imshow(corr_matrix,
                text_auto=True, 
                aspect="auto", 
                color_continuous_scale="RdBu",  # Usa una colormap valida
                labels=dict(color="Correlazione"))

fig.update_layout(title="Mappa di Calore Interattiva delle Correlazioni", 
                  xaxis_title="Variabili",
                  yaxis_title="Variabili")

# Mostrare la heatmap interattiva
fig.show()


#-------------


# Creare un line plot per il prezzo medio del biglietto in base alla classe di viaggio
fare_mean_per_class = df.groupby("Age")["Fare"].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.lineplot(x='Age', y='Fare', data=fare_mean_per_class, marker='o', linestyle='-', color='blue')
plt.xlabel('Classe di Viaggio')
plt.ylabel('Prezzo Medio del Biglietto (Fare)')
plt.title('Prezzo Medio del Biglietto per Classe di Viaggio (Line Plot)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

