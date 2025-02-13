
def leggiFile():
    with open("file.csv","r") as myFile:
        cont = myFile.read()
    
    return cont

def scriviFile(ele):
    with open("file.csv","w") as myFile:
        myFile.write(ele)
"""
conte = leggiFile()

righe = conte.split("\n")
tabella = []
for riga in righe:
    tabella.append(riga.split(","))

print(tabella[2][-1])

nuovariga =[]
for ele in range(3):
    nuovariga.append(input("Inserisci valore: "))

conte= ",".join(nuovariga)
scriviFile("\n"+conte)

conte = leggiFile()
nuovariga =[]
for ele in range(3):
    nuovariga.append(input("Inserisci valore: "))

conteN= ",".join(nuovariga)

conte+="\n"+conteN

scriviFile(conte)
"""
conte = leggiFile()

righe = conte.split("\n")
tabella = []
for riga in righe:
    tabella.append(riga.split(","))

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