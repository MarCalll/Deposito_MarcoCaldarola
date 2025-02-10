class Persona:
    def __init__(self,nome,eta):
        self.__nome = nome
        self.__eta = eta
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self,new_nome):
        self.__nome=new_nome
    
    def get_eta(self):
        return self.__eta
    
    def set_eta(self,new_eta):
        self.__eta=new_eta
    
    def presentazione(self):
        print("Sono", self.get_nome(),"ed ho", self.get_eta(),"anni.")
        
    def __str__(self):
        return f"{self.get_nome()} -- {self.get_eta()} anni."
        
class Studente(Persona):
    voti={}
    def __init__(self, nome, eta,voti):
        super().__init__(nome, eta)
        self.voti=voti
    
    def calcola_media(self):
        somma = 0
        for ele in self.voti.values():
            somma += ele
        return somma / len(self.voti) if self.voti else 0
    
    def dai_voto(self, materia, voto):
        self.voti[materia] = voto
        
    def presentazione(self):
        print("Sono", self.get_nome(),"ed ho", self.get_eta(),"anni. - media voto:",self.calcola_media())
    
    def __str__(self):
        return f"{self.get_nome()} -- {self.get_eta()} anni. - STUDENTE"

class Professore(Persona):
    def __init__(self, nome, eta,materia):
        super().__init__(nome, eta)
        self.materia = materia
        
    def presentazione(self):
        print("Sono", self.get_nome(),",ho", self.get_eta(),"anni e sono professore di",self.materia)
        
    def __str__(self):
        return f"{self.get_nome()} -- {self.get_eta()} anni. - PROFSSORE DI {self.materia}"

class Classe:
    professori=[]
    studenti=[]
    
    def __init__(self,classe,sezione):
        self.classe=classe
        self.sezione=sezione
        
    def descrizione(self):
        print("Classe",self.classe,"Sezione",self.sezione)
    
    def aggiungi_pro_stu(self):
        #aggiunge un professore o uno studente in base all'input
        scelta=int((input("Scegli cosa creare: 1.professore, 2.studente")))
        if scelta ==1:
            nome=(input("nome del professore: "))
            eta=int((input("età del professore: ")))
            materia=(input("materia del professore: "))
            nuovo_professore= Professore(nome,eta,materia)
            self.professori.append(nuovo_professore)            
        elif scelta ==2:
            nome=(input("nome dello studente: "))
            eta=int((input("età dello studente: ")))
            nuovo_studente= Studente(nome,eta,{})
            self.studenti.append(nuovo_studente)  
            
    def stampa_classe(self):
        #con un ciclo for stampa le liste dei professori e degli studenti
        print("Nome classe: ",self.classe,self.sezione)
        print("Professori:")
        for ele in self.professori:
            print(ele)
        print("Studenti:")
        for ele in self.studenti:
            print(ele)
            
    def assegna_voto(self):
        #crea una materia e un voto nel dizionario dello studente
        nome=(input("nome dello studente: "))
        materia=(input("materia: "))
        voto=int((input("voto: ")))
        for ele in self.studenti:
            if(ele.get_nome()==nome):
               ele.dai_voto(materia,voto)
               
    def mostra_voto_studente(self):
        #mostra la presentazione dello studente 
        nome=(input("nome dello studente: "))
        for ele in self.studenti:
            if ele.get_nome()==nome:
                ele.presentazione()

        
    def menu(self):
        condizione = True
        while condizione:
            print("-------------| Menu classe |-------------")
            print("1. Aggiungi professore/studente")
            print("2. Mostra classe")
            print("3. Assegna voto a studente")
            print("4. Mostra voti studente")
            print("5. Stop")
            
            scelta = int(input("Seleziona un'opzione: "))
            if scelta == 1:
                self.aggiungi_pro_stu()
            elif scelta == 2:
                self.stampa_classe()
            elif scelta == 3:
                self.assegna_voto()
            elif scelta == 4:
                self.mostra_voto_studente()
            elif scelta==5:
                condizione = False
                print("Programma terminato.")
            else:
                print("Opzione non valida! Riprova.")
    
class Scuola:
    classi=[]
    def __init__(self,nome):
        self.nome=nome
        
    def descrizione(self):
        print("Nome scuola:",self.nome)
        
    def aggiungi_classe(self):
        classe=(input("nome della classe: "))
        sezione=int((input("sezione della classe: ")))
        nuova_classe= Classe(classe,sezione)
        self.classi.append(nuova_classe)  
     
per=Studente("Marco",27,{"Matematica":2,"Inglese":4,"Italiano":6})
pro=Professore("Pippo",77,"Matematica")
classe=Classe(1,"B")
scuola=Scuola("Scuola delle merendine")

classe.menu()

