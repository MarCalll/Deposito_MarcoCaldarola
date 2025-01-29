#2
nome = "Marco"
print("Premi 1 per aggiungere")
print("Premi 2 per rimuovere")
print("Premi 3 per eliminare")
scelta = int(input("inserire un numero:"))
if(scelta==1):
    print("hai selezionato aggiungi")
    aggiunta = input()
    nome+=aggiunta
elif(scelta==2):
    print("hai selezionato rimuovi")
    nome=input()
elif(scelta==3):
    nome=""
    print("hai selezionato elimina")
else:
    print("valore non valido")