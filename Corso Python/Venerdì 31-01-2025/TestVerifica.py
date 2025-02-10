#6.Es 2:  Andare a creare un sistema ripetibile che si occupa di gestire la lunghezza delle stringhe e salvarle,l'utente potrà continuare a inserire dati finché la stringa 
#         inserita e più lunga della precedente, alla fine stamperà l'insieme delle stringhe date in input divise da virgole e quante stringhe ha inserito.

raccoglitoreStringhe = []

while True:
    stringa = input("Inserisci una stringa (o digita 'fine' per terminare): ")
    if stringa.lower() == 'fine':
        break
    
    if len(raccoglitoreStringhe) > 0:
        if len(stringa) > len(raccoglitoreStringhe[-1].split(" lunghezza: ")[0]):
            testo = stringa + " lunghezza: " + str(len(stringa)) + " caratteri"
            raccoglitoreStringhe.append(testo)
        else:
            print("La stringa inserita non è più lunga della precedente. Il programma si ferma.")
            break
    else:
        testo = stringa + " lunghezza: " + str(len(stringa)) + " caratteri"
        raccoglitoreStringhe.append(testo)

print(raccoglitoreStringhe)

print("Hai inserito",len(raccoglitoreStringhe), "stringhe.")

# Es 1: Crea un sistema ripetibile che si occupi di dividere su tre possibili liste i tipi basilari di dato che riceve in entrata. Deve poter stampare una lista singola o tutte.
# Si deve ripetere X volte definite all'inizio dall'utente

input_string = input("Inserisci una frase: ")

stringhe = []
interi = []
booleans = []
floats = []

for elemento in input_string.split():
    if elemento.isdigit():
        interi.append(int(elemento))
    elif elemento.replace('.', '', 1).isdigit() and elemento.count('.') < 2:
        floats.append(float(elemento))
    elif elemento.lower() == 'true' or elemento.lower() == 'false':
        booleans.append(elemento.lower() == 'true')
    else:
        stringhe.append(elemento)

print("Stringhe:", stringhe)
print("Interi:", interi)
print("Booleani:", booleans)
print("Float:", floats)






