#1
eta = int(input("Quanti anni hai?: "))
filmDisponibili = ["1.the mask","2.Batman","3.Spiderman"]

if eta>=18:
    print("Scegli il film da guardare")
    print(filmDisponibili)
    scelta = int(input())
    print("Hai selezionato",filmDisponibili[scelta-1])
else:
    print("Non puoi vedere questo film")
    
#2
while(True):
    primoNumero = int(input("Primo numero "))
    secondoNumero = int(input("Secondo numero "))
    operazione = input("Tipo di operazione(/,+,-,*)")
    risultato=0

    if operazione=="+" :
        risultato=primoNumero+secondoNumero
        print(risultato)
    elif operazione=="-" :
        risultato=primoNumero-secondoNumero
        print(risultato)
    elif operazione=="*" :
        risultato=primoNumero*secondoNumero
        print(risultato)
    elif operazione=="/" :
        if(primoNumero!=0 and secondoNumero!=0):
            risultato=primoNumero/secondoNumero
            print(risultato)
        else:
            print("Numero 0 non valido")
            break

    else: print("operazione",operazione,"non valida")

