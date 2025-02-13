def leggiFile():
    with open("sda.csv","r") as myFile:
        cont = myFile.read()
    
    return cont

def scriviFile(contenuto):
    with open("sda.csv","w") as myFile:
        myFile.write(contenuto)

conte = leggiFile()

righe = conte.split("\n")
tabella = []
for riga in righe:
    tabella.append(riga.split(","))


def aggiungi_alunno():
    nome = input("inserisci nome ")
    cognome = input("inserisci cognome ")
    with open("sda.csv", "a") as myFile:
        myFile.write(f"{nome},{cognome},0,0,0\n")

def modifica_alunno(tabella):
    cognEs = input("cosa vuoi sostituire: ")
    cognN = input("con cosa vuoi sostituire: ")


    trovato = False
    for indR in range(len(tabella)):
        if tabella[indR][1] == cognEs.lower():
            tabella[indR][1]= cognN.lower()
            trovato = True
            break
    if trovato:
        print("valore sostituito")
    else:
        print(f"valore {cognEs} non trovato!")
        
    righe = []
    for riga in tabella:
        righe.append(",".join(riga))

    conte = "\n".join(righe)

    scriviFile(conte)
    return tabella


def rimuovi_alunno(tabella):
    nome_esistente = input("Inserisci il nome dell'alunno ")
    cognome_esistente = input("Inserisci il cognome dell'alunno ")
    for indR in range(len(tabella)):
        if tabella[indR][0] == nome_esistente.lower() and tabella[indR][1] == cognome_esistente.lower():
            tabella.pop(indR)
            print("Alunno eliminato!")
            break
        else:
            print("Hai sbagliato qualcosa")
    
    righe = []
    for riga in tabella:
        righe.append(",".join(riga))

    conte = "\n".join(righe)


    scriviFile(conte)
    return tabella      
        



# rimuovi_alunno(tabella)

while True:
    scelta = input("""
Seleziona:
1 per aggiungere gli alunni;
2 per modificare gli alunni;
3 per eliminare gli alunni;
4 per uscire: """)
    if scelta == "1":
        aggiungi_alunno()
    elif scelta == "2":
        tabella = modifica_alunno(tabella)
    elif scelta == "3":
        tabella = rimuovi_alunno(tabella)
    elif scelta == "4":
        print("Grazie per aver usato il programma!")
        break
    else:
        print("Comando non valido!")

# tabella = modifica_alunno(tabella)

# aggiungi_alunno()

print(tabella)