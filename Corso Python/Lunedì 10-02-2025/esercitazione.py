"""
frase =input("Scrivimi una frase")
indice=0
for ele in frase:
    if ele=="a" or ele=="e" or ele=="i" or ele=="o" or ele=="u":
        print("vocale",ele,"indice:",indice)
    indice+=1



frase =input("Scrivimi una frase")
vocali=["a","e","i","o","u"]
indice=0
for ele in frase:
    if ele in vocali:
        print("vocale",ele,"indice:",indice)
    indice+=1
    
"""

frase =input("Scrivimi una frase")

caratteri={}

for ele in frase:
    caratteri[ele] = caratteri.get(ele, 0) + 1
    
print(caratteri)

#________________________________________________________

frase2 =input("Scrivimi una frase2")

caratteri={}

for ele in frase2:
    caratteri[ele] = 0

for ele in caratteri:
    for ele2 in frase2:
        if ele==ele2:
            caratteri[ele] +=1

print(caratteri)


frase3 =input("Scrivimi una frase3")

caratteri={}
for ele in frase3:
    if ele in caratteri:
        caratteri[ele]+=1
    else:
        caratteri[ele]=1
        
print(caratteri)


studenti = []

media = []

condizione = True
while condizione:
    print("-------------| Menu |-------------")
    print("1. Aggiungi studente e voto ")
    print("2. Mostra Studenti ")
    print("3. Stop")

    scelta = int(input("Seleziona un'opzione: "))

    if scelta == 1:
        nome = input("Inserisci nome alunno ")
        quantità_voti = int(input("Inserisci quanti voti vuoi: "))
        for pippo in range(quantità_voti):
            voto = int(input("Inserisci voto "))
            media.append(voto)
            voto_media = sum(media) / len(media)
        studenti.append({"Nome" : nome, "Media" : voto_media})
    elif scelta == 2:
        for i in studenti:
            print( "Nome: ", i["Nome"], ", Media:", i["Media"])
    elif scelta==3:
        condizione = False
        print("Programma terminato.")
    else:
        print("Opzione non valida! Riprova.")