import math

class Punto:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def muovi(self,newx,newy):
        self.x = newx
        self.y = newy
    def distanza_da_origine(self):
        distanza = math.sqrt(self.x**2 + self.y**2)
        print("Distanza del punto dall'origine: ",distanza)
        
        
punto1=Punto(4,2)
print(punto1.x)
print(punto1.y)
punto1.muovi(5,3)
print(punto1.x)
print(punto1.y)
punto1.distanza_da_origine()