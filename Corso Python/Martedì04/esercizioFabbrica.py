class Prodotto:
    def __init__(self, nome,costo_produzione,prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    
    def calcola_profitto(self):
        return self.prezzo_vendita-self.costo_produzione
    
    def get_nome(self):
        return self.nome
    
class Abbigliamento:
    def __init__(self, nome,costo_produzione,prezzo_vendita,materiale):
        self.prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale
        
    def calcola_profitto(self):
        return self.prodotto.calcola_profitto()
    
    def get_nome(self):
        return self.prodotto.nome
        
class Elettronica:
    def __init__(self, nome,garanzia,costo_produzione, prezzo_vendita):
        self.prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia
        
    def calcola_profitto(self):
        return self.prodotto.calcola_profitto()
    
    def get_nome(self):
        return self.prodotto.nome

class Fabbrica:
    inventario = {}
    profitto = 0.00
    
    def aggiungi_prodotto(self, prodotto):
        nome_prodotto = prodotto.get_nome()
        self.inventario[nome_prodotto] = {'prodotto': prodotto}
        print(f"Prodotto {nome_prodotto} aggiunto all'inventario.")
        
    def vendi_prodotto(self, nome_prodotto):
        if nome_prodotto in self.inventario:
            prodotto = self.inventario[nome_prodotto]['prodotto']
            profitto_prodotto = prodotto.calcola_profitto()
            self.profitto += profitto_prodotto
            del self.inventario[nome_prodotto]
            print(f"Prodotto {nome_prodotto} venduto. Profitto: {profitto_prodotto:.2f}€. Profitto totale: {self.profitto:.2f}€.")
        else:
            print(f"Il prodotto {nome_prodotto} non è presente nell'inventario.")
                        
# Test
prod1 = Prodotto("Test1", 123, 200)
prod2 = Prodotto("Test2", 456, 700)
fab = Fabbrica()
fab.aggiungi_prodotto(prod1)
fab.aggiungi_prodotto(prod2)
fab.vendi_prodotto("Test1")
fab.vendi_prodotto("Test2")
        