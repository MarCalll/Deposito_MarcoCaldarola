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
    
modo1=Paypal(2500)
modo2=CartaDiCredito(1500)
modo3=BonificoBancario(300)

gp=GestorePagamenti()
gp.paga(modo1,500)
gp.paga(modo2,1000)
gp.paga(modo3,200)

gp.mostra(modo1)
gp.mostra(modo2)
gp.mostra(modo3)
