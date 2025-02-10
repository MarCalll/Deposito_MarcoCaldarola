import random
#Esercizio Base
def giocoGeneraNumeroDa1a100():
    numeroCasuale=str(random.randint(1,101))
    print(numeroCasuale)
    while True:
        numeroUtente = input("Inserisci un numero o U per uscire: ")
        if numeroUtente.lower()=="u":
            print("Uscita dal gioco.")
            break
        if numeroUtente==numeroCasuale:
            print("Hai indovinato il numero,chiusura dell'applicazione")
            break
        elif numeroUtente>numeroCasuale:
            print("il numero è più piccolo di quello inserito")
        elif numeroUtente<numeroCasuale:
            print("il numero è più grande di quello inserito")
        else:
            print("input non valido")
    
#giocoGeneraNumeroDa1a100()

def fibonacci(numero):
    fibonacciList = [0, 1]
    numeroFibonacci = fibonacciList[-1] + fibonacciList[-2]
    for i in range(2, numero):
        if numeroFibonacci >= numero:
            break
        fibonacciList.append(numeroFibonacci)
        numeroFibonacci = fibonacciList[-1] + fibonacciList[-2]
    return fibonacciList

# print(fibonacci(int(input("Inserisci un numero"))))