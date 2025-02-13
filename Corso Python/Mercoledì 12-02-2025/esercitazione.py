def build_header():
    with open("tabella.csv", "w") as myFile:
        myFile.write(f"nome,cognome,voto 1,voto 2,voto 3")
        
def leggiFile():
    with open("tabella.csv","r") as myFile:
        cont = myFile.read()
    return cont

def scriviFile(ele):
    with open("tabella.csv","w") as myFile:
        myFile.write(ele)

def aggiungi_alunno():
    nome = input("inserisci nome")
    cognome = input("inserisci cognome")
    voto_1 = input("inserisci voto_1")
    voto_2 = input("inserisci voto_2")
    voto_3 = input("inserisci voto_3")
    with open("tabella.csv", "a") as myFile:
        myFile.write(f"\n{nome},{cognome},{voto_1},{voto_2},{voto_3}")

def cambio_voto(posizione,tabella):
    nome = input("Nome dell'alunno ")
    cognome = input("Cognome dell'alunno ")
    cambio = input("cambiare voto1 in cosa? ")
    for riga in tabella[1:]:
        if riga[0]==nome and riga[1]==cognome:
            riga[posizione]=cambio
            print("Cambiato")

def cambio_nome_cognome(posizione,tabella):
    nome_da_cambiare = input("nome da cambiare? ")
    cambio = input("cambiare in cosa? ")
    for riga  in tabella[1:]:
        if riga [posizione]==nome_da_cambiare:
            riga [posizione]=cambio
            print("Cambiato")

def modifica_alunno_nome_cognome(tabella):
    condizione=True
    while condizione:
        
        dato = input("nome,cognome,voto1,voto2,voto3 ").lower()
        if dato=="nome":
            
            cambio_nome_cognome(0,tabella)
            condizione=False
            
        elif dato=="cognome":
            
            cambio_nome_cognome(1,tabella)
            condizione=False
            
        elif dato=="voto1":
            cambio_voto(2,tabella)
            condizione=False
        
        elif dato=="voto2":
            cambio_voto(3,tabella)
            condizione=False
            
        elif dato=="voto3":
            cambio_voto(4,tabella)
            condizione=False
            
        else:
            print("Input non valido")
            
    righe = []
    for riga in tabella:
        righe.append(",".join(riga))

    conte = "\n".join(righe)

    scriviFile(conte)

def rimuovi_alunno(tabella):
    nome = input("Nome dell'alunno da eliminare")
    cognome = input("Cognome dell'alunno da eliminare")
    print(tabella)
    for riga in tabella[1:]:
        print(riga)
        if riga[0]==nome and riga[1]==cognome:
            print(riga)
            tabella.remove(riga)
    
    righe = []
    for riga in tabella:
        righe.append(",".join(riga))
    conte = "\n".join(righe)
    scriviFile(conte)

def menu():
    condizione = True
    while condizione:

        fileLetto = leggiFile()
        tabella = [riga.split(",") for riga in fileLetto.strip().split("\n")]

        print("\n-------------| MENU |-------------")
        print("1. Aggiungi alunno")
        print("2. Modifica alunno")
        print("3. Rimuovi alunno")
        print("4. Reset tabella")
        print("5. Visualizza alunni")
        print("6. Stop")


        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            aggiungi_alunno()
        elif scelta == "2":
            modifica_alunno_nome_cognome(tabella)
        elif scelta == "3":
            rimuovi_alunno(tabella)
        elif scelta == "4":
            build_header()
            print("Tabella resettata con successo!")
        elif scelta == "5":
            for ele in tabella[1:]:
                print(f"Nome Alunno: {ele[0]}, Cognome Alunno: {ele[1]}, Voto1: {ele[2]}, Voto2: {ele[3]}, Voto3: {ele[4]},Media: {sum([int(ele[2]),int(ele[3]),int(ele[4])])/3}")
        elif scelta=="6":
            condizione = False
            print("Programma terminato.")
        else:
            print("Opzione non valida! Inserisci un numero tra 1 e 5.")


menu()
