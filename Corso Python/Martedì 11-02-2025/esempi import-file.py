"""
import random as rd
import libre
from lib .libre import somma
somma(5,10)

from random import randint, choice

#print(randint(0,1000))

lista = [5,11,6,1,99,22]

print(choice(lista))


from datetime import date, datetime

print(date(2025,2,11))
print(datetime(2025,2,11,14,57,0))
print(datetime.now())

numero = input("inserisci un numero: ")
try:
    for num in range(int(numero)):
        print("ciao!")
except:
    print("numero non valido, hai scritto:",numero)

print("proseguo programma!")


with open("prova.txt","a") as mioFile:
    mioFile.write("ciao\n")

with open("prova.txt","r") as mioFile:
    contenuto = mioFile.read()
print(contenuto)

with open("prova.txt","w") as mioFile:
    mioFile.write("ciao\n")
"""
with open("prova.txt","x") as mioFile:
    pass

with open("file.csv","r") as fileCsv:
    contenuto = fileCsv.read()

print(contenuto.split("\n")[1].split(",")[0])