class MetodoPagamento:
    def __init__(self,importo_base):
        self.importo_base = importo_base
        
    def effettua_pagamento(self,importo):
        self.importo_base-=importo
        
    def mostra_importo(self):
        print(self.importo_base)
    
class CartaDiCredito(MetodoPagamento):
    pass
    
class Paypal(MetodoPagamento):
    pass
    
class BonificoBancario(MetodoPagamento):
    pass

class GestorePagamenti:
    def paga(self,gestore:MetodoPagamento,quantità):
        gestore.effettua_pagamento(quantità)
    
    def mostra(self,gestore:MetodoPagamento):
        gestore.mostra_importo()

class Banca:
    
    gestore=GestorePagamenti()
    
    def __init__(self,nome_utente,password,metodoPagamento):
        self.nome_utente=nome_utente
        self.password=password
        self.metodoPagamento=metodoPagamento
    
    def menu(self):
        print("LOGIN RIUSCITO")
        condizione = True
        while condizione:
            print("1. Effettua pagamento")
            print("2. Mostra importo")
            print("3. Stop")
            scelta = int(input("Seleziona un'opzione: "))
            if scelta == 1:
                quantita = int(input("1. Quantità da pagare "))
                self.gestore.paga(self.metodoPagamento,quantita)
            elif scelta == 2:
                print("L'importo è di:")
                self.gestore.mostra(self.metodoPagamento)
            elif scelta==3:
                condizione = False
                print("Programma terminato.")
            else:
                print("Opzione non valida! Riprova.")
    
    def logInMenu(self):
        print("LOGIN")
        nome_utente=(input("Inserire nome utente: "))
        password=(input("inserire password: "))
        if nome_utente==self.nome_utente and password==self.password:
            self.menu()
        else:
            print("Login fallito")

banca=Banca("Pippo","Baudo",BonificoBancario(500))
banca.logInMenu()
