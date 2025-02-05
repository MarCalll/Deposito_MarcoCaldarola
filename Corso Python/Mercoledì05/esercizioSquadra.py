class MembroSquadra:
    def __init__(self, nome,eta):
        self.nome = nome
        self.eta = eta
        
    def descrivi(self):
        print("Questo è ",self.nome ,"di età", self.eta ,"anni")
    
    def __str__(self):
        return f"{self.nome} - {self.eta} anni"

class Giocatore(MembroSquadra):
    def __init__(self, nome, eta,ruolo,numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
    
    def __str__(self):
        return f"{self.nome} - {self.eta} anni - {self.ruolo}"
    
class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza=anni_di_esperienza
    
    def __str__(self):
        return f"{self.nome} - {self.eta} anni - {self.anni_di_esperienza} anni di esperienza"

class Assistente(MembroSquadra):
    def __init__(self, nome, eta,specializzazione):
        super().__init__(nome, eta)
        self.specializzazione=specializzazione
        
    def __str__(self):
        return f"{self.nome} - {self.eta} anni - Specializzazione {self.specializzazione}"

class Squadra():
    lista_giocatori=[]
    lista_allenatori=[]
    lista_assistenti=[]
    
    def __init__(self,nome_squadra):
        self.nome_squadra=nome_squadra
        
    def aggiungi_giocatore(self,giocatore):
        self.lista_giocatori.append(giocatore)
        
    def aggiungi_allenatore(self,allenatore):
        self.lista_allenatori.append(allenatore)
    
    def aggiungi_assistenti(self,assistenti):
        self.lista_assistenti.append(assistenti)
    
    def mostra_squadra(self):
        print("Lista di giocatori:")
        for ele in self.lista_giocatori:
            print(ele)
        print("Lista di allenatori:")
        for ele in self.lista_allenatori:
            print(ele)
        print("Lista di assistenti:")
        for ele in self.lista_assistenti:
            print(ele)
    
    def crea_membro_squadra(self):
        scelta=int((input("Scegli cosa creare: 1.giocatore, 2.allenatore, 3.assistente ")))
        if scelta ==1:
            nome=(input("Scegli il nome del giocatore: "))
            eta=int((input("Scegli l'età del giocatore: ")))
            ruolo=(input("Scegli il ruolo del giocatore: "))
            numero_maglia=(input("Scegli il numero maglia del giocatore: "))
            nuovo_Giocatore= Giocatore(nome,eta,ruolo,numero_maglia)
            self.aggiungi_giocatore(nuovo_Giocatore)
        elif scelta ==2:
            nome=(input("Scegli il nome dell'allenatore: "))
            eta=int((input("Scegli l'età dell'allenatore: ")))
            anni_di_esperienza=(input("Scegli gli anni d'esperienza dell'allenatore: "))
            nuovo_Allenatore= Allenatore(nome,eta,anni_di_esperienza)
            self.aggiungi_allenatore(nuovo_Allenatore)
        elif scelta ==3:
            nome=(input("Scegli il nome dell'assistente: "))
            eta=int((input("Scegli l'età dell'assistente: ")))
            specializzazione=(input("Scegli la specializzazione dell'assistente: "))
            nuovo_Assistente= Assistente(nome,eta,specializzazione)
            self.aggiungi_assistenti(nuovo_Assistente)
                        
    def rimuovi_membro_squadra(self):
        nome=(input("inserire il nome di chi rimuovere:"))
        for ele in self.lista_giocatori:
            if ele.nome==nome:
                self.lista_giocatori.remove(ele) 
        for ele in self.lista_allenatori:
            if ele.nome==nome:
                self.lista_allenatori.remove(ele) 
        for ele in self.lista_assistenti:
            if ele.nome==nome:
                self.lista_assistenti.remove(ele) 
            
    def menu(self):
        condizione = True
        while condizione:
            print("-------------| Menu |-------------")
            print("1. Aggiungi membro squadra")
            print("2. Mostra membri squadra")
            print("3. Rimuovi membri squadra")
            print("4. Stop")
            
            scelta = int(input("Seleziona un'opzione: "))
            if scelta == 1:
                self.crea_membro_squadra()
            elif scelta == 2:
                self.mostra_squadra()
            elif scelta == 3:
                self.rimuovi_membro_squadra()
            elif scelta == 4:
                condizione = False
                print("Programma terminato.")
            else:
                print("Opzione non valida! Riprova.")

        
    
kaka = Giocatore("Kaka",42,"Centrocampista",8)
lippi= Allenatore("Lippi",76,40)
pippo= Assistente("Pippo",42,"Psicologo")
sq1=Squadra("Squadra1")
sq1.aggiungi_giocatore(kaka)
sq1.aggiungi_allenatore(lippi)
sq1.aggiungi_assistenti(pippo)

sq1.menu()
