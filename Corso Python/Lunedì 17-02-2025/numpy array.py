import numpy as np

x=4
y=4

x+y


#-------------





#-------------


# Creazione di un array unidimensionale
arr = np.array([1, 2, 3, 4, 5])

# Creazione di un array bidimensionale
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

arr


#-------------


arr2d


#-------------


# Creazione di un array
arr = np.array([1, 2, 3, 4, 5])

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape) # Output: (5,)
print("Dimensioni dell'array:", arr.ndim) # Output: 1
print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr.size) # Output: 5
print("Somma degli elementi:", arr.sum()) # Output: 15
print("Media degli elementi:", arr.mean()) # Output: 3.0
print("Valore massimo:", arr.max()) # Output: 5
print("Indice del valore massimo:", arr.argmax()) # Output: 4


#-------------


es1 = np.arange(10,70)
print(es1)
print(es1.dtype)
es1_cambiato = es1.astype('float64') 
print(es1_cambiato.dtype)
print(es1_cambiato.shape)
es1_tridimensionale = es1_cambiato.reshape(3,4,5)
print(es1_tridimensionale)
print(es1_tridimensionale.ndim)


#-------------


arr = np.arange(7,15) # 1,2,3,4,5

print(arr)

# Indexing
print(arr[0])

# Slicing
print(arr[:2])

# Boolean Indexing
print(arr[arr > 9])


#-------------


arr_2d = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
# Slicing sulle righe
print(arr_2d[1:3]) # Output: [[ 5 6 7 8]
# [ 9 10 11 12]]
# Slicing sulle colonne
print(arr_2d[:, 1:3]) # Output: [[ 2 3]
# [ 6 7]
# [10 11]]
# Slicing misto
print(arr_2d[1:, 1:3]) # Output: [[ 6 7]
# [10 11]]


#-------------


import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing di base
print(arr[2:7])  # Output: [2 3 4 5 6]

# Slicing con passo
print(arr[1:8:2])  # Output: [1 3 5 7]

# Omettere start e stop
print(arr[:5])  # Output: [0 1 2 3 4]
print(arr[5:])  # Output: [5 6 7 8 9]

# Utilizzare indici negativi
print(arr[-5:])  # Output: [5 6 7 8 9]
print(arr[:-5])  # Output: [0 1 2 3 4]


#-------------


arr = np.array([10, 20, 30, 40, 50])

# Utilizzo di un array di indici
indices = np.array([1, 3])
print(arr[indices])  # Output: [20 40]

# Utilizzo di una lista di indici
indices = [0, 2, 4]
print(arr[indices])  # Output: [10 30 50]


#-------------


# Esercizio su NumPy Slicing

# Consegna:
# Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
# Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
# Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
# Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
# Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
# Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
# Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.

# Obiettivo:
# Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e modificare sottoarray specifici da un array più grande.

es1 = np.random.randint(10, 51, 20)
print(es1)
es2 = es1[:10]
print(es2)
es2 = es1[-5:]
print(es2)
# es3 = np.random.randint(10, 51, 20)
es1[4:10] = 99
print(es1)


#-------------


# Consegna:
# Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
# Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
# Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
# Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
# Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
# Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita, la diagonale principale e la matrice invertita modificata.

# Obiettivo:
# Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, modificare e manipolare sotto-matrici e array, applicando operazioni avanzate come
# l'inversione delle righe e la sostituzione condizionale degli elementi.

num_casuali = np.random.randint(1, 100, 72)
num_2D = num_casuali.reshape(2,6,6)
print(num_2D)
sotto_matrice_centrale = num_2D[:, 1:5, 1:5]
print("\n","\n","\n", sotto_matrice_centrale)
sotto_matrice_centrale_invertita = sotto_matrice_centrale[:, ::-1, :]
print("\n","\n","\n", sotto_matrice_centrale_invertita)
diagonale = np.array([np.diagonal(piano) for piano in sotto_matrice_centrale_invertita])
diag_1D = diagonale.reshape(1,4,2)
print("\n","\n","\n", diag_1D)
sotto_matrice_centrale_invertita[sotto_matrice_centrale_invertita % 3 == 0] = -1
print("\n","\n","\n", sotto_matrice_centrale_invertita)






#-------------


arr = np.array([1, 2, 3, 4, 5])

sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)

print("Sum:", sum_value)    # Output: Sum: 15
print("Mean:", mean_value)  # Output: Mean: 3.0
print("Standard Deviation:", std_value)  
# Output: Standard Deviation: 1.4142135623730951

