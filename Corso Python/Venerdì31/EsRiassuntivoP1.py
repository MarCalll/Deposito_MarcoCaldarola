#

def creaAccount():
    nomeUtente=input("Inserire nuovo nome utente: ")
    password=input("Inserire password: ")
    return [nomeUtente,password,[]]

#account=creaAccount()

def aggiungiNumero(account):
    numero=input("Inserire nuovo numero di telefono: ")
    account[2].append([numero])
    print(account)
    
#aggiungiNumero()

def checkNomeUtente(nuovoNomeUtente,account):
    if account[0]==nuovoNomeUtente:
        return True
    else:
        return False

def cambioNomeUtente(account):
    print("Cambio Nome utente: ")
    nuovoNomeUtente=input("Inserisci nuovo nome utente ")
    if checkNomeUtente(nuovoNomeUtente,account)==False:
        print("nome utente cambiato")
        account[0]=nuovoNomeUtente
        print(account)
    else:
        print("Nome utente già esistente")
        
#cambioNomeUtente()

def controllaNumeriTelefono(account):
    print("Questi sono i numeri di telefono:")
    contatore=0
    for i in account[2]:
        print(i)
        contatore+=1
    print("ci sono",contatore,"numeri di telefono")
    

    