import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Percorso del file CSV
file_path = 'imdb_top_1000.csv'

# Caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)

#le prime righe del DataFrame per confermare
print(df.head())

df

df.isnull().sum()
df.info()

df_pieno = df["Gross"].dropna()
df_pieno

df_pieno = df_pieno.str.replace(",", "").astype(int)
df_pieno
media_gross = df_pieno[1].mean().astype(float)
media_gross

df['Meta_score'] = df['Meta_score'].fillna(df['Meta_score'].mean())
df['Gross'] = df['Gross'].str.replace(",", "").astype(float)
df['Gross'] = df['Gross'].fillna(media_gross)
# df.isnull().sum()
df

df.info()

df.describe()

correlation_matrix = df.select_dtypes(include=["number"]).corr()
correlation_matrix
plt.figure(figsize =(10,6))
sns.heatmap(correlation_matrix, annot = True, cmap ="coolwarm", fmt = ".3f", linewidths =1)
plt.show()

mean_Gross_byGenre = df.groupby(df['Genre'].str.split(",", n=1).str[0])['Gross'].mean()
mean_Gross_byGenre

df['IMDBGroup'] = pd.cut(df['IMDB_Rating'], bins=[7.6, 8.0, 8.5, 9.0, 9.3], right=False)
mean_Gross_byIMDB = df.groupby('IMDBGroup')['Gross'].mean()
mean_Gross_byIMDB

df['Runtime'] = df['Runtime'].str.replace(" min", "").astype(int)

df[df["Gross"] == df["Gross"].min()]

df[df["Gross"] == df["Gross"].max()]

has_duplicates = df['Series_Title'].duplicated().any()
has_duplicates

duplicate_rows = df[df['Series_Title'].duplicated()]
duplicate_rows

duplicates_by_id = df[df.duplicated(subset=['Series_Title'], keep=False)]
duplicates_by_id

registi_presenti = df['Director'].value_counts()
registi_presenti

gen_freq = df['Genre'].str.split(",", n=1).str[0].value_counts()
gen_freq

gen_freq2 = df['Genre'].value_counts()
gen_freq2

df['Certificate'].unique()

df['Certificate'] = df['Certificate'].fillna('Unrated')
cert_freq = df['Certificate'].value_counts()
cert_freq


top_IMDB = df[df ['IMDB_Rating'] > 8.5]
sorted_top = top_IMDB.sort_values('IMDB_Rating', ascending=True)
sorted_top

num_top = sorted_top['IMDB_Rating'].count()
num_top

df[df["IMDB_Rating"] == df["IMDB_Rating"].max()]

df[df["IMDB_Rating"] == df["IMDB_Rating"].min()]

df[df["Meta_score"] == df["Meta_score"].max()]

df[df["Meta_score"] == df["Meta_score"].min()]

top_10_IMDBRating = df.sort_values('IMDB_Rating', ascending=False).head(10)
top_10_IMDBRating

top_10_Voti = df.sort_values('No_of_Votes', ascending=False).head(10)
top_10_Voti

top_10_Incasso = df.sort_values('Gross', ascending=False).head(10)
top_10_Incasso

df_contronto = pd.DataFrame({
    'Film con più incassi': top_10_Incasso['Series_Title'].reset_index(drop=True),
    'Film con più voti': top_10_Voti['Series_Title'].reset_index(drop=True),
    'Film con miglior IMDBRating': top_10_IMDBRating['Series_Title'].reset_index(drop=True)
})
df_contronto

df['IMDBGroup'] = pd.cut(df['IMDB_Rating'], bins=[7.6, 8.0, 8.5, 9.0, 9.3], right=False)
mean_Votes_byIMDB = df.groupby('IMDBGroup')['No_of_Votes'].mean()
mean_Votes_byIMDB

df['IMDBGroup'] = pd.cut(df['IMDB_Rating'], bins=[7.6, 8.0, 8.5, 9.0, 9.3], right=False)
mean_Gross_byIMDB = df.groupby('IMDBGroup')['Gross'].mean()
mean_Gross_byIMDB

mean_IMDBRating_byGenre = df.groupby(df['Genre'].str.split(",", n=1).str[0])['IMDB_Rating'].mean()
mean_IMDBRating_byGenre

mean_Runtime_byGenre = df.groupby(df['Genre'].str.split(",", n=1).str[0])['Runtime'].mean()
mean_Runtime_byGenre

mean_Gross_byGenre = df.groupby(df['Genre'].str.split(",", n=1).str[0])['Gross'].mean()
mean_Gross_byGenre

Film_per_anno = df['Released_Year'].value_counts()
Film_per_anno

PG = df[df['Released_Year'] == 'PG']
PG

df['Released_Year'] = df['Released_Year'].str.replace("PG", "1995")
df['Released_Year'] = df['Released_Year'].astype(int)

df['Decenni'] = pd.cut(df['Released_Year'], bins=range(1900, 2030, 10), right=True)
mean_IMDBR_byDecenni = df.groupby('Decenni')['IMDB_Rating'].mean()
mean_IMDBR_byDecenni

df.info()

# Qual è il film con il rating più alto per ogni decennio?
mean_IMDBRmax_byDecenni = df.groupby('Decenni', observed=True)['IMDB_Rating'].idxmax()
mean_IMDBRmax_byDecenni

migliori_dec = df[['Series_Title','Released_Year', 'Decenni']].iloc[[321,126,51,32,4,12,1,15,0,2,18]]
migliori_dec

mean_IMDBR_byDirector = df.groupby('Director')['IMDB_Rating'].mean()
mean_IMDBR_byDirector

attori_presenti1 = df['Star1'].value_counts()
attori_presenti2 = df['Star2'].value_counts()
attori_presenti3 = df['Star3'].value_counts()
attori_presenti4 = df['Star4'].value_counts()
top_attori = pd.concat([attori_presenti1, attori_presenti2, attori_presenti3, attori_presenti4], axis=1).sum(axis=1).sort_values(ascending=False).astype(int)
top_attori.head(10)

df['MetaGroup'] = pd.cut(df['Meta_score'], bins=range(0,101,5), right=True)
Metascore_pergruppi = df.groupby('MetaGroup')['Series_Title'].count()
Metascore_pergruppi

top_MetaS = df[df ['Meta_score'] > 95] 

attori_presenti_topfilm1 = top_MetaS['Star1'].value_counts()
attori_presenti_topfilm2 = top_MetaS['Star2'].value_counts()
attori_presenti_topfilm3 = top_MetaS['Star3'].value_counts()
attori_presenti_topfilm4 = top_MetaS['Star4'].value_counts()
attori_presenti_topfilm = pd.concat([attori_presenti_topfilm1, attori_presenti_topfilm2, attori_presenti_topfilm3, attori_presenti_topfilm4], axis=1).sum(axis=1).sort_values(ascending=False).astype(int)
attori_presenti_topfilm.head(20)

top_IMDBRAT = df [df['IMDB_Rating'] > 9]

attori_presenti_topfilm1 = top_IMDBRAT['Star1'].value_counts()
attori_presenti_topfilm2 = top_IMDBRAT['Star2'].value_counts()
attori_presenti_topfilm3 = top_IMDBRAT['Star3'].value_counts()
attori_presenti_topfilm4 = top_IMDBRAT['Star4'].value_counts()
attori_presenti_topfilm = pd.concat([attori_presenti_topfilm1, attori_presenti_topfilm2, attori_presenti_topfilm3, attori_presenti_topfilm4], axis=1).sum(axis=1).sort_values(ascending=False).astype(int)
attori_presenti_topfilm.head(20)

