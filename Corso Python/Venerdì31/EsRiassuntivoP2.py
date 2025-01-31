#2
import EsRiassuntivoP1

def decoratore_ciclo(funzione):
    def wrapper(*args, **kwargs):
        while True:
            scelta = input("Scrivi 'chiudi' per terminare, premi qualsiasi tasto per continuare: ")
            if scelta == "chiudi":
                print("Programma terminato.")
                break
            funzione(*args, **kwargs)
    return wrapper

def decoratore_saluto(funzione):
    def wrapper(*args, **kwargs):
        print("Benvenuto nel programma!")
        funzione(*args, **kwargs)
        print("Addio!")
    return wrapper

@decoratore_saluto
@decoratore_ciclo
def esegui_operazioni():
    account = EsRiassuntivoP1.creaAccount()
    EsRiassuntivoP1.aggiungiNumero(account)
    EsRiassuntivoP1.cambioNomeUtente(account)
    EsRiassuntivoP1.controllaNumeriTelefono(account)

esegui_operazioni()