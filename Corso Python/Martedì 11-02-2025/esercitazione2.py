#Scrivete un programma che utilizza il cifrario di Cesare per criptare una
#parola o decriptarla.

#Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
#ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
#sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
#di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
#una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
#Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
#conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
#di posti corrispondente alla chiave.

def cripta(parola,chiave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    nuovaparola=""
    
    for lettera in parola:
        if lettera in alfabeto:
            indice = alfabeto.index(lettera)
            nuovo_indice = (indice + chiave) % len(alfabeto)
            print((indice + chiave), "%", len(alfabeto))
            print(nuovo_indice)
            nuovaparola += alfabeto[nuovo_indice]
        else:
            nuovaparola += lettera
            
    print(nuovaparola)
    
def decripta(parola, chiave):
    alfabeto = "abcdefghijklmnopqrstuvxyz"
    nuovaparola = ""
    
    for lettera in parola:
        if lettera in alfabeto:
            indice = alfabeto.index(lettera)
            nuovo_indice = (indice - chiave) % len(alfabeto)
            nuovaparola += alfabeto[nuovo_indice]
        else:
            nuovaparola += lettera
    
    print(nuovaparola)
    
def menu():
        condizione = True
        while condizione:
            print("\n-------------| Menu |-------------")
            print("1. Cripta frase")
            print("2. Decripta frase")
            print("3. Stop")

            scelta = input("Seleziona un'opzione: ")

            if scelta == "1":
                frase = input("scrivi frase da criptare: ")
                chiave = int(input("scrivi chiave: "))
                cripta(frase,chiave)

            elif scelta == "2":
                frase_cripta = input("Scrivi frase da decriptare: ")
                chiave = int(input("Scrivi chiave: "))
                decripta(frase_cripta, chiave)

            elif scelta == "3":
                condizione = False
                print("Programma terminato.")

            else:
                print("Opzione non valida! Riprova.")

menu()