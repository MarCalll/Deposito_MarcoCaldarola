#3
nomeutente=""
password=""

if(nomeutente=="" and password==""):
    
    placeholderNU = input("registra nuovo utente:")
    placeholderP = input("inserisci password:")
    placeholderNU = nomeutente
    placeholderP = password
    
    if(nomeutente==placeholderNU and password==placeholderP):
        print("utente già esistente inserire un campo valido:")
        placeholderNU = input("registra nuovo utente:")
        placeholderP = input("inserisci password:")
        nomeutente= placeholderNU
        password= placeholderP

else:
    print("utente già esistente")
        
    
    
    