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
        
class Studente(Persona):
    voti=[]
    def __init__(self, nome, eta,voti):
        super().__init__(nome, eta)
        self.voti=voti
    
    def calcola_media(self):
        somma=0
        for ele in self.voti.values():
            somma+=ele
        return somma/len(self.voti)
        
    def presentazione(self):
        print("Sono", self.get_nome(),"ed ho", self.get_eta(),"anni. - media voto:",self.calcola_media())

class Professore(Persona):
    def __init__(self, nome, eta,materia):
        super().__init__(nome, eta)
        self.materia = materia
        
    def presentazione(self):
        print("Sono", self.get_nome(),",ho", self.get_eta(),"anni e sono professore di",self.materia)

class Classe:
    Professori=[]
    Studenti=[]
    
class Scuola:
    classi=[]
     
per=Studente("Marco",27,{"Matematica":2,"Inglese":4,"Italiano":6})
pro=Professore("Pippo",77,"Matematica")

per.presentazione()
pro.presentazione()