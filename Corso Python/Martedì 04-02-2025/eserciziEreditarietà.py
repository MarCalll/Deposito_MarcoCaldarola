class Animale:
    def __init__(self,nome,eta):
        self.nome=nome
        self.eta=eta

    def fai_suono(self):
        print("*verso generico*")

class Cane(Animale):
    def fai_suono(self):
        print("*BAUUU*")
    def scodinzola(self):
        print("il cane scodinzola")
     
class Gatto(Animale):
    def fai_suono(self):
        print("*MIAOO*")
    def caccia(self):
        print("il gatto caccia")
        
class Papera(Animale):
    def __init__(self, nome, eta,becco):
        super().__init__(nome, eta)
        self.becco=becco
    def fai_suono(self):
        print("*QUACK*")
    def lung_becco(self):
        print("lunghezza becco:",self.becco,"cm")
        
anim=Gatto("Ciro",43)
anim.fai_suono()
anim.caccia()
anim=Papera("Pippo",13,13)
anim.fai_suono()
anim.lung_becco()