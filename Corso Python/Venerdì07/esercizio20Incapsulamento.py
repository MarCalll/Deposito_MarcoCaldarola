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
            
    def menu_parco_veicoli(self):
        condizione = True
        while condizione:
            print("-------------| Menu Parco Veicoli |-------------")
            print("1. Aggiungi veicolo")
            print("2. Rimuovi veicolo")
            print("3. Lista veicoli")
            print("4. Stop")
            
            scelta = int(input("Seleziona un'opzione: "))
            if scelta == 1:
                creazione=int((input("Scegli cosa creare: 1.Auto, 2.Motocicletta, 3.Furgone")))
                if scelta ==1:
                    marca=input("marca: ")
                    modello=input("modello: ")
                    anno=int(input("anno: "))
                    nauto=Auto(marca,modello,anno)
                    self.aggiungi_veicolo(nauto)
                elif scelta ==2:
                    marca=input("marca: ")
                    modello=input("modello: ")
                    anno=int(input("anno: "))
                    tipo=input("tipo: ")
                    nmoto=Motocicletta(marca,modello,2023,tipo)
                    self.aggiungi_veicolo(nmoto)
                elif scelta ==3:
                    marca=(input("marca: "))
                    modello=int((input("modello: ")))
                    anno=(input("anno: "))
                    capca=(input("capca: "))
                    nfurg=Furgone(marca,modello,anno,capca)
                    self.aggiungi_veicolo(nfurg)
            elif scelta == 2:
                marca=input("marca da rimuovere: ")
                modello=input("modello da rimuovere: ")
                self.rimuovi_veicolo(marca,modello)
            elif scelta == 3:
                self.lista_veicoli()
            elif scelta == 4:
                condizione = False
                print("Programma terminato.")
            else:
                print("Opzione non valida! Riprova.")
        
gpv=GestioreParcoVeicoli()
gpv.menu_parco_veicoli()
