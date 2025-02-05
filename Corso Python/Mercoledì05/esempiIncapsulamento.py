class Persona:
    __nome="Mirko"
    def getNome(self):
        return self.__nome
    def setNome(self,newNome):
        self.__nome=newNome

mio=Persona()

#print(mio.__nome)
print(mio.getNome())
mio.setNome("Test")
print(mio.getNome())