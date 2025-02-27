
#-------------


import pandas as pd
import numpy as np

file_path = 'imdb_top_1000.csv'
df = pd.read_csv(file_path)

# Mostrare le prime righe del dataset
df.head()


#-------------


# Controllare i valori mancanti
missing_values = df.isnull().sum() #valori booleani e somma di questi ultimi

df.isnull().sum()


#-------------


# rimuovo la colonna 'Certificate' dal DataFrame
df.drop(columns=['Certificate'], inplace=True)

df.head()


#-------------


meta_score_mean = df['Meta_score'].mean()
df.head()


#-------------


df['Gross'] = df['Gross'].str.replace(',', '', regex=True).astype(float) #pulisce la colonna gross, sostituzione delle virgole con una stringa vuota, conversione stringa a numerico float
gross_mean = df['Gross'].mean()

gross_mean


#-------------


df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce').astype('Int64') #conversioni in valori numerici di released year, se ci sono valori non numerici vengono trasmormati in NaN
df.head()


#-------------


df["Runtime"] = df["Runtime"].astype(str).str.replace(" min", "").astype(float).astype('Int64') #cinversione in string, rimozione min, conversione colonna in numeri interi

df.describe()


#-------------





#-------------





#-------------





#-------------


df["Gross"] = df["Gross"].astype(str).str.replace(",", "").astype(float) #conversione gross in string, rimovendo le virgole
df.describe()


#-------------


num_duplicati = df.duplicated().sum() #serie booleana e somma dei duplicati
print("Numero di film duplicati:", num_duplicati)
film_duplicati = df[df.duplicated(keep=False)]
print("Film duplicati:")
print(film_duplicati)


#-------------


registi_contati = df['Director'].value_counts() #conto il numero di film
registi_multipli = registi_contati[registi_contati > 1] #registi che hanno fatto piu di un film
num_registi_multipli = registi_multipli.count() #conto quanti sono i registi multipli
num_registi_multipli


#-------------


# calcolo la durata media dei film in minuti
durata_media = df["Runtime"].mean()
durata_media



#-------------


#calcolo il voto medio IMDB di tutti i film
voto_medio_imdb = df["IMDB_Rating"].mean()
voto_medio_imdb


#-------------


# conto i film con un IMDB rating superiore a 8.5
num_film_alti_voti = df[df["IMDB_Rating"] > 8.5].shape[0]
num_film_alti_voti


#-------------


film_rating_piu_alto = df[df["IMDB_Rating"] == df["IMDB_Rating"].max()]
film_rating_piu_alto


#-------------


film_rating_piu_basso = df[df["IMDB_Rating"] == df["IMDB_Rating"].min()]
film_rating_piu_basso


#-------------


film_duplicati = df[df.duplicated(keep=False)] #false indica che tutte le copie di una riga devono essere considerate un duplicato
if film_duplicati.empty:
    print("Non ci sono film perfettamente duplicati nel dataset.")
else:
    print("Film perfettamente duplicati trovati:")
    print(film_duplicati)


#-------------


df_ratingelevato = df.sort_values(by="IMDB_Rating", ascending=False) #ordina il dataframe in base alla colonna, ordinamento decrescente
top_10_film = df_ratingelevato.head(9)
print("Top 10 film con il rating IMDB più alto:")
print(top_10_film[["Series_Title", "Released_Year", "IMDB_Rating", "Director"]])


#-------------


# ordino il dataFrame in base al numero di voti in ordine decrescente
df_ordinato_voti = df.sort_values(by="No_of_Votes", ascending=False)
# selezionare i primi 10 film con il maggior numero di voti
top_10_voti = df_ordinato_voti.head(10)
print("Top 10 film con il maggior numero di voti:")
print(top_10_voti[["Series_Title", "Released_Year", "IMDB_Rating", "No_of_Votes", "Director"]])


#-------------


# ordino il DataFrame in base al valore di incasso in ordine decrescente
df_ordinato_gross = df.sort_values(by="Gross", ascending=False)
#seleziono i primi 10 film con il maggior incasso
top_10_gross = df_ordinato_gross.head(10)

print("Top 10 film con il maggior incasso:")
print(top_10_gross[["Series_Title", "Released_Year", "IMDB_Rating", "Gross", "Director"]])


#-------------


# ordino il dataFrame per IMDB_Rating (dal più alto al più basso)
df_ordinato_rating = df.sort_values(by="IMDB_Rating", ascending=False)

# ordino il dataFrame per No_of_Votes (dal più alto al più basso)
df_ordinato_voti = df.sort_values(by="No_of_Votes", ascending=False)

# stampo i primi 10 film in entrambe le classifiche per confrontare
print(" Top 10 film per Rating IMDB:")
print(df_ordinato_rating.head(10)[["Series_Title", "IMDB_Rating", "No_of_Votes"]])

print("\n Top 10 film per Numero di Voti:")
print(df_ordinato_voti.head(10)[["Series_Title", "IMDB_Rating", "No_of_Votes"]])



#-------------


# seleziono i titoli dei primi 10 film per entrambe le classifiche
top_10_rating = set(df_ordinato_rating.head(10)["Series_Title"])
top_10_voti = set(df_ordinato_voti.head(10)["Series_Title"])
# identificare i film presenti in entrambe le liste
film_comuni = top_10_rating.intersection(top_10_voti)
film_comuni


#-------------


#creo fasce di rating (ogni 0.5 punti)
df['RatingGroup'] = pd.cut(df['IMDB_Rating'], bins=[7.5, 8, 8.5, 9, 9.5, 10], right=False) #suddivisione della colonno numerica di rating in intervalli di 0.5

#calcolo il numero medio di voti per ciascun gruppo di rating
mean_votes_by_ratinggroup = df.groupby('RatingGroup')['No_of_Votes'].mean() #raggruppo i dati per fasce di rating
print("Numero medio di voti per ogni fascia di rating IMDB:")
print(mean_votes_by_ratinggroup)


#-------------


genre_counts = df['Genre'].value_counts()

print("Genere più frequente nel dataset:")
print(genre_counts.head(10))


#-------------


mean_rating_by_genre = df.groupby('Genre')['IMDB_Rating'].mean() #raggruppo per genere e poi seleziono il rating per calcolare la media
print("Rating medio per genere:")
print(mean_rating_by_genre)


#-------------


mean_Runtime_by_genre = df.groupby('Genre')['Runtime'].mean()
print(" Durata media dei film per ogni genere:")
print(mean_Runtime_by_genre)


#-------------


mean_Gross_by_genre = df.groupby('Genre')['Gross'].mean()
print(" Media profitto per genere")
print(mean_Gross_by_genre)


#-------------


films_per_year = df['Released_Year'].value_counts()
most_frequent_year = films_per_year.idxmax() #indice è l'anno e il valore è il numero di film
num_films = films_per_year.max() #valore massimo di film della serie
print(f"l'anno con il maggior numero di film nel dataset è il {most_frequent_year} con {num_films} film.")


#-------------


df['Decadegroup']= pd.cut(df['Released_Year'], bins=range(1920,2026,10), right=False) #suddivisione della colonno numerica di rating in intervalli di 0.5
#calcolo il numero medio di voti per ciascun gruppo di rating
mean_rating_by_decade = df.groupby('Decadegroup')['IMDB_Rating'].mean() #raggruppo i dati per fasce di rating
print("Rating IMBD per decennio:")
print(mean_rating_by_decade)


#-------------


rating_piu_alto_decennio = df.groupby('Decadegroup')['IMDB_Rating'].idxmax()
rating_piu_alto_decennio


#-------------


df.loc[rating_piu_alto_decennio, ["Series_Title","Released_Year","IMDB_Rating"]]


#-------------


director_counts = df['Director'].value_counts() #conta quante volte appare ogni regista nel dataset

print("Registi con il maggior numero di film nel dataset:")
print(director_counts.head(10)) 


#-------------


rating_medio_regista= df.groupby('Director')['IMDB_Rating'].mean()
rating_medio_regista


#-------------


conteggio_attori = pd.concat([df['Star1'],df['Star2'],df['Star3'],df['Star4']])
conteggio_attori


#-------------


conta_tutti=conteggio_attori.value_counts()
conta_tutti.head(9)


#-------------





#-------------





#-------------


conteggio_attoriprova1 = df['Star1'].value_counts()
conteggio_attoriprova2 = df['Star2'].value_counts()
conteggio_attoriprova3 = df['Star3'].value_counts()
conteggio_attoriprova4 = df['Star4'].value_counts()

conteggio_totale_attori= (conteggio_attoriprova1
                          .add(conteggio_attoriprova2, fill_value=0)
                          .add(conteggio_attoriprova3, fill_value=0)
                          .add(conteggio_attoriprova4, fill_value=0))
conteggio_totale_attori.sort_values(ascending=False).head(9)


#-------------


df['Scoregroup']= pd.cut(df['Meta_score'], bins=range(28,100,5), right=False) #suddivisione della colonno numerica di rating in intervalli di 0.5
#calcolo il numero medio di voti per ciascun gruppo di rating
count_score = df.groupby('Scoregroup')['Series_Title'].count() #raggruppo i film
count_score


#-------------


df.describe()


#-------------


film_alto_rating = df[df['Meta_score'] >=90]
attori = pd.concat([df['Star1'],df['Star2'],df['Star3'],df['Star4']]).value_counts()
attori     


#-------------


import seaborn as sns
import matplotlib.pyplot as plt


correlation_matrix = df.select_dtypes(include=["number"]).corr()
correlation_matrix
plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()


#-------------


dfold = df[df["Released_Year"]<1980]

correlation_matrix = dfold.select_dtypes(include=["number"]).corr()
correlation_matrix
plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()


#-------------


dfold = df[df["Released_Year"]>1980]

correlation_matrix = dfold.select_dtypes(include=["number"]).corr()
correlation_matrix
plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()


#-------------


dfold = df[df["Released_Year"]<1960]

correlation_matrix = dfold.select_dtypes(include=["number"]).corr()
correlation_matrix
# plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()


#-------------


import pandas as pd
import numpy as np
df['5anni']= pd.cut(df['Released_Year'], bins=range(1920,2026,5), right=True) #suddivisione della colonno numerica di rating in intervalli di 0.5
#calcolo il numero medio di voti per ciascun gruppo di rating
mean_gross_by_5anni = df.groupby('5anni')['Meta_score'].mean() #raggruppo i dati per fasce di rating
print(mean_gross_by_5anni)


#-------------


import pandas as pd
import numpy as np
df['10metascore']= pd.cut(df['Meta_score'], bins=range(0,101,10), right=True) #suddivisione della colonno numerica di rating in intervalli di 0.5
#calcolo il numero medio di voti per ciascun gruppo di rating
mean_No_of_Votes_by_10metascore = df.groupby('10metascore')['No_of_Votes'].mean() #raggruppo i dati per fasce di rating
print(mean_No_of_Votes_by_10metascore)


#-------------


import pandas as pd
import numpy as np
df['10metascore']= pd.cut(df['Meta_score'], bins=range(0,101,10), right=True) #suddivisione della colonno numerica di rating in intervalli di 0.5
#calcolo il numero medio di voti per ciascun gruppo di rating
mean_No_of_Votes_by_10metascore = df.groupby('10metascore')['No_of_Votes'].mean() #raggruppo i dati per fasce di rating
print(mean_No_of_Votes_by_10metascore)

