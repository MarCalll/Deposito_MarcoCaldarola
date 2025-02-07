class Veicolo:
    _accensione=False
    variabile="globale"
    
    def __init__(self,marca,modello,anno):
        self._marca=marca
        self._modello=modello
        self._anno=anno
        
    def accendi(self):
        self._accensione=True
        
    def spegni(self):
        self.accensione=False
        
    def __str__(self):
        return f"{self._marca} - {self._modello} - {self._anno}"
    
    def funz_variabile_glob(self):
        variabile="locale"
        print(variabile)
        def variabileNON():
            nonlocal variabile
            non="non"
            variabile=non+variabile
            print(variabile)
        variabileNON()
        print(variabile)
        
class Auto(Veicolo):
    _numero_porte=4
    def suona_clacson(self):
        print("*DOOT DOOT*")
        
class Furgone(Veicolo):
    __carico=[]
    def __init__(self, marca, modello, anno,capacita_carico):
        super().__init__(marca, modello, anno)
        self._capacita_carico=capacita_carico
        
    def set_carico(self,oggetto):
        self.__carico.append(oggetto)
        
    def get_carico(self):
        print(self.__carico)
        
    def carica(self):
        print("Sto caricando...")
    
    def carica(self):
        print("Sto scaricando...")
        
class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno,tipo):
        super().__init__(marca, modello, anno)
        self._tipo=tipo
        
    def esegui_wheelie(self):
        if self._tipo=="sportivo":
            print("Fai impennata")
        else:
            print("Niente impennata")
            
class GestioreParcoVeicoli:
    _veicoli=[]
    
    def aggiungi_veicolo(self,veicolo):
        self._veicoli.append(veicolo)
    
    def rimuovi_veicolo(self,marca,modello):
        for ele in self._veicoli:
            if ele._marca==marca and ele._modello==modello:
                self._veicoli.remove(ele)
    
    def lista_veicoli(self):
        print("Lista veicoli")
        for ele in self._veicoli:
            print(ele)
        
    
auto1=Auto("BMW","Serie 3",2021)
moto1=Motocicletta("Yamaha","YZF-R1",2023,"Sportiva")
furg1=Furgone("Mercedes-Benz","Sprinter 316 CDI",2022,1500)

gpv=GestioreParcoVeicoli()
gpv.aggiungi_veicolo(auto1)
gpv.aggiungi_veicolo(moto1)
gpv.lista_veicoli()
gpv.rimuovi_veicolo("BMW","Serie 3")
gpv.lista_veicoli()

furg1.set_carico("Televisore")
furg1.get_carico()

print(furg1.variabile)
furg1.funz_variabile_glob()

