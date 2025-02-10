frase =input("Scrivimi una frase")
vocali=["a","e","i","o","u"]
indice=0
for ele in frase:
    if ele in vocali:
        print("vocale",ele,"indice:",indice)
    indice+=1