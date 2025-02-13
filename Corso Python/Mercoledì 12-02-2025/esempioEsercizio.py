def inizio():
    fileT = False
    try:
        with open("dbAl.txt","r") as dbFile:
            contenuto = dbFile.read()
        fileT = True
    except:
        contenuto= "nome,cognome,voto1,voto2,voto3"
    righe = contenuto.split("\n")
    tabella = [riga.split(",") for riga in righe]
    return tabella, fileT

def scriviFile(tabella):
    righe = [",".join(riga) for riga in tabella]
    contenuto = "\n".join(righe)
    with open("dbAl.txt","w") as dbFile:
        dbFile.write(contenuto)
    print("file scritto!")

def inserisciAlunno(tabella):
    nuovoAl =[]
    nome = input("inserisci il nome dell'alunno: ")
    nuovoAl.append(nome)
    cognome = input("inserisci il cognome dell'alunno: ")
    nuovoAl.append(cognome)
    for n in range(3):
        voto = input("inserisci un voto: ")
        nuovoAl.append(voto)
    tabella.append(nuovoAl)
    scriviFile(tabella)
    return tabella, True

def eliminaAlunno(tabella, fileT):
    if fileT:
        nomeS = input("inserisci il nome dell'alunno da modificare: ")
        cognomeS = input("inserisci il cognome dell'alunno da modificare: ")
        aluT = False
        for indiceR in range(len(tabella)):
            if tabella[indiceR][0].lower() == nomeS.lower() and tabella[indiceR][1].lower() == cognomeS.lower():
                tabella.pop(indiceR)
                aluT = True
                break
        if aluT:
            scriviFile(tabella)
            print("alunno eliminato!")
        else:
            print("alunno non trovato!")
        
        return tabella
    else:
        print("nessun alunno presente!")
        return tabella

def visualizzaAlunni(tabella,fileT):
    if fileT:
        for riga in tabella[1:]:
            print(f"Nome Alunno: {riga[0]}, Cognome Alunno: {riga[1]}, Voto1: {riga[2]}, Voto2: {riga[3]}, Voto3: {riga[4]}, Media: {sum([int(riga[2]),int(riga[3]),int(riga[4])])/3}")
    else:
        print("nessun alunno presente!")
print("Benvenuto nel programma di gestione studenti!\n")
tabella, fileT = inizio()
while True:
    scelta =input("""
Seleziona:
1 per visualizzare gli alunni;
2 per inserire alunni;
3 per eliminare alunni;
4 per uscire: """)
    if scelta == "1":
        visualizzaAlunni(tabella,fileT)
    elif scelta == "2":
        tabella, fileT = inserisciAlunno(tabella)
    elif scelta == "3":
        tabella = eliminaAlunno(tabella, fileT)
    elif scelta == "4":
        print("Grazie per aver usato il programma!")
        break
    else:
        print("Comando non valido!")

        

#tabella, fileT = inserisciAlunno(tabella, fileT)
#tabella = eliminaAlunno(tabella)
#visualizzaAlunni(tabella,fileT)