
condizione = True
while condizione:
    print("-------------| Menu |-------------")
    print("1. Check Palindromo")
    print("3. Stop")

    scelta = int(input("Seleziona un'opzione: "))

    if scelta == 1:
        frase = input("Inserisci frase da controllare: ")
        punteggiatura=";, "
        for ele in punteggiatura:
            frase=frase.replace(ele,"")
        #listafrase=[]
        #listafrasereverse=[]
        #for ele in frase:
        #    listafrase.append(ele)
        #listafrasereverse = listafrase[::-1]
        if frase==frase[::-1]:
            print("è palindroma")
        else:
            print("non è palindroma")
    elif scelta==2:
        condizione = False
        print("Programma terminato.")
    else:
        print("Opzione non valida! Riprova.")