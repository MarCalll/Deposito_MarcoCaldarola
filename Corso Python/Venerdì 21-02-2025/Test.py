import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Percorso del file CSV
file_path = 'avocado.csv'

# Caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)

#le prime righe del DataFrame per confermare 
df.head()

df.info()

#Voglio sapere in quale periodo si sono venduti più avocado.
TopVolumeTotaleAvocado=df[df["region"]=="TotalUS"].sort_values(by="Total Volume", ascending=False).head(10)
TopVolumeTotaleAvocado

#Voglio sapere in quale periodo si sono venduti la minor quantità di avocado.
BottomVolumeTotaleAvocado=df[df["region"]=="TotalUS"].sort_values(by="Total Volume", ascending=True).head(10)
BottomVolumeTotaleAvocado

# Matrice senza le righe TotalUS
#regionFiltrate = ['TotalUS', 'West', 'Plains', 'Midsouth', 'Southeast', 'GreatLakes', 'Northeast']
#dfNoTotalUS = df[~df['region'].isin(regionFiltrate)]
dfNoTotalUS = df[(df['region'] != 'TotalUS') & (df['region'] != 'West') & (df['region'] != 'Plains') & (df['region'] != 'Midsouth') & (df['region'] != 'Southeast') & (df['region'] != 'GreatLakes') & (df['region'] != 'Northeast')]
correlation_matrix =dfNoTotalUS.select_dtypes(include=["number"]).corr()
plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()

#Osservazioni:
# 1. Total Volume - Avarage Price : correlazione debole che potrebbe stare ad indicare che più richiesta c'è di avocado meno verranno a costare o viceversa
#     quando i prezzi sono più bassi, più persone li comprano

# 2. AveragePrice - i vari tipi di avocado: la correlazione conferma che un aumento del prezzo medio porta a una diminuzione delle vendite per tutti
#     i tipi di avocado, avvalorando il punto 1, in più:
#     la tipologia 4046 ha una correlazione negativa relativamente forte con il prezzo medio, il che suggerisce che questa varietà tende a essere meno
#     costosa quando il prezzo medio è più basso.

#     la tipologia 4225 ha una correlazione simile, sebbene leggermente inferiore a quella di 4046, indicando che anche questa varietà tende
#     a essere venduta a un prezzo relativamente più basso.

#     la tipologia 4770 suggerisce che questa varietà potrebbe essere più costosa rispetto alle altre due.

# 3. Correlazione tra i tipi di avocado: potrebbe stare a significare che i vari tipi di avocado tendono ad essere venduti insieme e i tipi 4046 e 4225 
#     sono più popolari del 4770.
#     Anche tutti i tipi di avocado seguono la stessa tendenza con l'avarage price e total volume: quando il prezzo medio aumenta, le vendite diminuiscono

# 4. Total Bags - small bags: ha una correlazione fortissima con Small Bags questo starebbe a significare che la maggior parte degli avocado viene venduta 
#     in sacchetti piccoli

# Raggruppamento per fasce di prezzo
df['AveragePricegroup']= pd.cut(df['AveragePrice'], bins=range(0,5,1), right=False)
mean_avaragepricegroup_by_Volume = df.groupby('AveragePricegroup', observed=True)['Total Volume'].mean()
print(mean_avaragepricegroup_by_Volume)
#Il risultato dimostra che con l'aumentare del prezzo le vendite diminuiscono

# Scatter plot per visualizzare la relazione
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='AveragePrice', y='Total Volume')
plt.title('Scatter Plot di Total Volume vs Average Price')
plt.xlabel('Average Price')
plt.ylabel('Total Volume')
plt.show()
#Questo scatter plot dimostra come a prezzi bassi c'è una maggiore domanda

# volume medio per tipo di avocado rispetto al prezzo medio
volume_price_tipo = df.groupby(['AveragePrice'])[['4046', '4225', '4770']].mean()

# prezzo medio per il quale il volume è massimo per ciascun tipo di avocado
volume_price_4046 = volume_price_tipo.loc[volume_price_tipo['4046'] == volume_price_tipo['4046'].max()]
volume_price_4225 = volume_price_tipo.loc[volume_price_tipo['4225'] == volume_price_tipo['4225'].max()]
volume_price_4770 = volume_price_tipo.loc[volume_price_tipo['4770'] == volume_price_tipo['4770'].max()]

print("\n-------------------- volume_price_4046 -------------------- \n",volume_price_4046)
print("\n-------------------- volume_price_4225 -------------------- \n",volume_price_4225)
print("\n-------------------- volume_price_4770 -------------------- \n",volume_price_4770)

#confronto volume massimi tra i 3 tipi di avocado 

# tipo di avocado con max volume totale
volume_per_tipo = df[['4046', '4225', '4770']].sum()
print(volume_per_tipo)

# Questo grafico dimostra che si sceglievano le tipologie 4046 e 4225(comunque le tipologie più economiche come dimostrato nella matrice).

#Top 10 regioni che hanno acquistato più avocado?
volumeGroupByRegion = dfNoTotalUS.groupby(['region'])["Total Volume"].mean()
top_10_regions = volumeGroupByRegion.sort_values(ascending=False).head(10)
top_10_regions

#regioni che hanno acquistato più avocado organici?
df_organic=dfNoTotalUS[dfNoTotalUS["type"]=="organic"]
regions_organic= df_organic.groupby(['region'])["Total Volume"].mean().sort_values(ascending=False).head(10)
print("\nregioni che hanno acquistato più avocado organici?\n\n",regions_organic)
#regioni che hanno acquistato più avocado convenzionali?
df_conv=dfNoTotalUS[dfNoTotalUS["type"]=="conventional"]
regions_conv = df_conv.groupby(['region'])["Total Volume"].mean().sort_values(ascending=False).head(10)
print("\nregioni che hanno acquistato più avocado convenzionali?\n\n",regions_conv)
#Sono stati venduti molti più avocado convenzionali che biologici, i cambiamenti si vedono dal quinto posto in poi

#Andamento volume avocado negli anni organici e convenzionali negli anni

dfNoTotalUS = dfNoTotalUS.copy()
dfNoTotalUS['Date'] = pd.to_datetime(dfNoTotalUS['Date'])

df_organic = dfNoTotalUS[dfNoTotalUS['type'] == 'organic'].copy()
df_2020org = df_organic[df_organic['Date'].dt.year <= 2020]
volumeGroupByDate_2020organic = df_2020org.groupby('Date')['Total Volume'].mean()

df_conv = dfNoTotalUS[dfNoTotalUS['type'] == 'conventional'].copy()
df_2020conv = df_conv[df_conv['Date'].dt.year <= 2020]
volumeGroupByDate_2020conv = df_2020conv.groupby('Date')['Total Volume'].mean()

plt.figure(figsize=(12, 3))
plt.plot(volumeGroupByDate_2020organic.index, volumeGroupByDate_2020organic.values, color='green', label='Biologico')
plt.title('Andamento del Volume di Avocado Biologici negli anni')
plt.xlabel('Data')
plt.ylabel('Volume Medio')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(12.29, 3))
plt.plot(volumeGroupByDate_2020conv.index, volumeGroupByDate_2020conv.values, color='orange', label='Convenzionale')
plt.title('Andamento del Volume di Avocado Convenzionali negli anni')
plt.xlabel('Data')
plt.ylabel('Volume Medio')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()


#Osservazioni:
# Nel 2017 gli avocado biologici nonostante la loro quantità molto minore rispetto a quelli convenzionali, rimangono relativamente stabili con qualche 
# fluttuazione, e crescono di popolarità.
# Invece per quelli convenzionali c'è molta più fluttuazione. 
# Si possono notare anche per entrambi picchi intorno a febbraio-marzo e giugno-luglio ogni anno
# 

df['Date'] = pd.to_datetime(dfNoTotalUS['Date'])
df_2020 = df[df['Date'].dt.year <= 2020]
priceGroupByDate_2020 = df_2020.groupby(['Date'])['AveragePrice'].mean()
volumeGroupByDate_2020 = df_2020.groupby(['Date'])['Total Volume'].mean()

fig, ax1 = plt.subplots(figsize=(12, 5))
ax1.set_xlabel('Data')
ax1.set_ylabel('Prezzo Medio', color='tab:red')
ax1.plot(priceGroupByDate_2020.index, priceGroupByDate_2020.values, color='tab:red', label="Prezzo Medio")
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.set_ylabel('Volume Medio', color='tab:blue')
ax2.plot(volumeGroupByDate_2020.index, volumeGroupByDate_2020.values, color='tab:blue', label="Volume Medio")
ax2.tick_params(axis='y', labelcolor='tab:blue')

plt.title('Andamento del Prezzo Medio e del Volume degli Avocado nel Tempo')
fig.tight_layout()
plt.grid(True)
plt.show()

# in questo grafico si puo notare come nei periodi in cui il prezzo è oiù basso gli acquisti sono molto più alti

df['type'] = df['type'].astype('category')
df['Avocado_Type'] = df['type'].cat.codes
df[['type', 'Avocado_Type']].head()

# Creare un pair plot per analizzare le relazioni tra variabili numeriche
plt.figure(figsize=(10, 6))
sns.pairplot(df.select_dtypes(include=['number']), hue='Avocado_Type', palette='coolwarm', corner=True)
plt.show()