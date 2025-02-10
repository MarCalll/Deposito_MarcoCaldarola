class CPU:
    def __init__(self,nome,microprocessori):
        self.nome=nome
        self.microprocessori=microprocessori
    
class RAM:
    def __init__(self,nome,Vram):
        self.nome=nome
        self.Vram=Vram
    
class Computer(CPU,RAM):
    def __init__(self,nome_cpu,microprocessori,nome_ram,Vram):
        CPU.__init__(self,nome_cpu,microprocessori)
        RAM.__init__(self,nome_ram,Vram)
    
    def desc_componenti(self):
        print("pc composto da ",self.nome, self.Vram)
        
pc = Computer("Gaming CPU", 8,"GAMING RAM", 16)
pc.desc_componenti()