#1
"""
numero = int(input("Inserisci un numero: "))
if numero % 2 == 0:
    print("Il numero in input è pari")
else:
    print("Il numero è dispari")
""" 


"""
#2
numero=int(input("Inserisci un numero: "))
while numero<=0 :
    numero = int(input("Inserisci un numero: "))

for i in range(numero,-1,-1):
    print(i)
    
"""


"""
#3
quantitaNumeri = int(input("Inserisci quanti numeri vuoi: "))
numeriLista=[]

for i in range(quantitaNumeri):
    numero = int(input("Inserisci il numero: "))
    numeriLista.append(numero **2)
    
print(numeriLista)
"""

#4
quantitaNumeri = int(input("Inserisci quanti numeri vuoi: "))
numeriLista=[]
numeroMaggiore=0
for i in range(quantitaNumeri):
    numero = int(input("Inserisci il numero: "))
    numeriLista.append(numero)
for i in numeriLista:
    if i>numeroMaggiore:
        numeroMaggiore=i
print(numeroMaggiore, "è il numero più grande")


contatore = 0
indice = 0
while indice < len(numeriLista):
    contatore += 1
    indice += 1   
print("La lista contiene", contatore, "numeri.")


numeroMaggiore2=0
contatore2=0
if(len(numeriLista)==0):
    print("Lista vuota")
else:
    for i in numeriLista:
        contatore2 += 1
        if i>numeroMaggiore2:
            numeroMaggiore2=i
print(numeroMaggiore2, "è il numero più grande")
print("Ci sono",contatore2,"numeri nella lista")
    