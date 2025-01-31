class Automobile:
    numero_di_ruote = 4
    def __init__(self, marca,modello):
        self.marca = marca
        self.modello = modello
        
    def stampa_info(self):
        print("l'automobile è una", self.marca, self.modello)
        
auto2 = Automobile("Fiat","500")
auto1 = Automobile("BMW","X3")

auto1.stampa_info()
auto2.stampa_info()
        