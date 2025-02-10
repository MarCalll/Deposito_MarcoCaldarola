class Posto:
    _occupato=False
    def __init__(self,numero,fila,occupato):
        self._numero=numero
        self._fila=fila
        self._occupato=occupato
        
    def prenota(self):
        if self._occupato == False:
            self._occupato=True
        else:
            print("Posto già occupato")
    
    def libera(self):
        if self._occupato==True:
            self._occupato=False
        else:
            print("Posto già libero")
            
    def getter(self):
        if self._occupato == True:
            stato="Occupato"
        else:
            stato="Libero"
        print("Numero posto:",self._numero, "- Fila:",self._fila,"- Stato:", stato)

    def __str__(self):
        if self._occupato == True:
            stato="Occupato"
        else:
            stato="Libero"
        return f"Numero posto: {self._numero} - Fila: {self._fila} - Stato: {stato}" 

class PostoVIP(Posto):
    def __init__(self, numero, fila, occupato,serviziExtra):
        super().__init__(numero, fila, occupato)
        self.servizi_extra = serviziExtra
        
    def prenota(self):
        print("Posto vip comprende:",self.servizi_extra)
        return super().prenota()

class PostoStandard(Posto):
    def __init__(self, numero, fila, occupato,costo):
        super().__init__(numero, fila, occupato)
        self._costo=costo
        
    def prenota(self):
        print("Costo:",self._costo)
        return super().prenota()
    
    def __str__(self):
        if self._occupato == True:
            stato="Occupato"
        else:
            stato="Libero"
        return f"Numero posto: {self._numero} - Fila: {self._fila} - Stato: {stato} - VIP" 
    
class Teatro:
    _posti=[]
    
    def __init__(self,posti):
        self._posti=posti
    
    def aggiungi_posto(self,posto):
        self._posti.append(posto)
    
    def stampa_posti_occupati(self):
        for ele in self._posti:
            print(ele)
    
    def prenota_posto(self,numero,fila):
        for ele in self._posti:
            if ele._numero == numero and ele._fila == fila:
                print("Posto trovato")
                ele.prenota()
                break
            else:
                pass
    
    def controlla_posto(self,Posto):
        print(Posto)
    
    def quantita_posti(self):
        print(len(self._posti))
        
    def menu_teatro(self):
        condizione = True
        while condizione:
            print("-------------| Menu Teatro |-------------")
            print("1. Stampa posti occupati")
            print("2. Prenota posto")
            print("3. Quantità posti")
            print("4. Stop")
            
            scelta = int(input("Seleziona un'opzione: "))
            if scelta == 1:
                self.stampa_posti_occupati()
            elif scelta == 2:
                numero=int(input("numero: "))
                fila=input("fila: ")
                self.prenota_posto(numero,fila)
            elif scelta == 3:
                self.quantita_posti()
            elif scelta == 4:
                condizione = False
                print("Programma terminato.")
            else:
                print("Opzione non valida! Riprova.")
        
     
pStandard2C=PostoStandard(2,"C",False,150)
pStandard3B=PostoStandard(3,"B",True,160)
pVIP=PostoVIP(4,"C",False,["Accesso al lounge","Servizio in posto"])
teatro=Teatro([pVIP,pStandard2C,pStandard3B])

teatro.controlla_posto(pStandard3B)
teatro.menu_teatro()
