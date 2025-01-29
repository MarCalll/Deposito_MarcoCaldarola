#simulazione login 
nomeUtente=""
password=""
colorePreferito=""
animalePreferito=""

nomeUtente = input("inserisci nuovo nome utente:")
password = input("inserisci nuova password")

print("Login")
nomeUtenteField = input("inserisci nome utente:")
passwordField = input("inserisci password")

if(nomeUtente==nomeUtenteField and password==passwordField):
    print("Benvenuto", nomeUtente)
    print("1.Scegli domanda segreta")
    print("2.Modifica nome utente")
    print("3.Modifica password")
    scelta = int(input())
    if(scelta==1):
        print("1.Qual'è il tuo colore preferito?")
        print("2.Qual'è il tuo animale preferito?")
        scelta = int(input())
        if(scelta==1):
            print("Scrivi colore preferito")
            colorePreferito = input()
        if(scelta==2):
            print("Scrivi animale preferito")
            animalePreferito = input()
    if(scelta==2):
        print("Modifica nome utente:")
        nomeUtente=input("inserisci nuovo nome utente:")
    if(scelta==3):
        print("Modifica password:")
        password=input("inserisci nuova password:")
else:
    print("Nome utente o password non valide")