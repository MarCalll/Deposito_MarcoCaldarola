numero = int(input("Inserisci un numero: "))
newNumero=numero
condizione=True
print(numero)

while (condizione):
    numero-=1
    print(numero)
    if(numero==0):
        scelta = input("Vuoi ripetere? Rispondere con Si o No ")
        if(scelta=="No"):
            condizione=False
        elif(scelta=="Si"):
            numero=newNumero
            print(numero)

#2
contatorePrimi = []

while len(contatorePrimi) < 5:
    numeroEs2 = int(input("Inserisci un numero: "))

    if numeroEs2 > 1:
        for i in range(2, int(numeroEs2**0.5) + 1):
            if numeroEs2 % i == 0:
                print("Il numero non è primo")
                break
        else:
            print("Il numero è primo")
            contatorePrimi.append(numeroEs2) 
    else:
        print("Il numero non è primo")

    if numeroEs2 % 2 == 0:
        print("Il numero in input è pari")
    else:
        print("Il numero è dispari")
        
    