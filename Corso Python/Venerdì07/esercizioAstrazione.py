from abc import ABC, abstractmethod

class Impiegato:
    def __init__(self,nome,cognome,stipendio):
        self.nome = nome
        self.cognome=cognome
        self.stipendio=stipendio
        
    @abstractmethod
    def calcola_stipendio():
        pass
    
    def __str__(self):
        return f"{self.nome} {self.cognome}, stipendio: {self.calcola_stipendio()}"
    
class ImpiegatoFisso(Impiegato):
    def calcola_stipendio(self):
        return self.stipendio
    
class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio,vendite):
        super().__init__(nome, cognome, stipendio)
        self.vendite=vendite
        
    def calcola_stipendio(self):
        bonus=(self.vendite*20)/100
        return self.stipendio+bonus

class Lavoro:
    def __init__(self,impiegati:list):
        self.impiegati=impiegati
  
    def stipendio_impiegati(self):
        for ele in self.impiegati:
            print(ele)
  
nino=ImpiegatoFisso("Nino","Rossi",1300) 
pino=ImpiegatoAProvvigione("Pino","Bianchi",1100,400)  
lavoro=Lavoro([nino,pino])

lavoro.stipendio_impiegati()