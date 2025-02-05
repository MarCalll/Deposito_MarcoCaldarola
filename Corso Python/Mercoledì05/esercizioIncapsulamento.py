class Banca:
    
    __conti_bancari=[]
    
    def __init__(self,nomeBanca):
        self.nomeBanca = nomeBanca
    
    def set_conti_bancari(self,new_conto_bancario):
        self.__conti_bancari.append(new_conto_bancario)
        
    def get_conti_bancari(self):
        for ele in self.__conti_bancari:
            print(ele)
        
    def crea_conto_bancario(self,titolare_CB):
        newCB = ContoBancario(titolare_CB)
        self.set_conti_bancari(newCB)
        return newCB
        
    def aggiungi_saldo_conto_bancario(self):
        chi=input("A quale utente aggiungere saldo")
        for ele in self.__conti_bancari:
            if ele.get_titolare() == chi:
                quanto=int(input("Quantità da aggiungere"))
                ele.deposita(quanto)
                
    def preleva_da_conto_bancario(self):
        chi=input("Da quale utente prelevare saldo?")
        for ele in self.__conti_bancari:
            if ele.get_titolare() == chi:
                quanto=int(input("Quantità da prelevare"))
                ele.preleva(quanto)
        

class ContoBancario:
    __saldo=0
    def __init__(self, titolare):
        self.__titolare = titolare
    
    def __str__(self):
        return f"Utente: {self.__titolare} - Saldo {self.__saldo} Euro"
    
    def get_titolare(self):
        return self.__titolare
    
    def set_titolare(self,newTitolare):
        self.__titolare = newTitolare
        
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self,newSaldo):
        self.__saldo = newSaldo
    
    def deposita(self,importo):
        if self.get_saldo()>=0:
            self.set_saldo(self.get_saldo()+importo)
        else:
            print("Numero negativo! Impossibile prelevare.")
    
    def preleva(self,prelievo):
        if prelievo<=self.get_saldo():
            self.set_saldo(self.get_saldo()-prelievo)
        else:
            print("Impossibile prelevare, prelievo più alto del saldo di", self.get_saldo()-prelievo, "euro" )
    
    def visualizza_saldo(self):
        print(self.get_saldo(), "euro depositati su questo conto.")
      
      
bancadeipoveri=Banca("Banca dei poveri")
bancadeipoveri.crea_conto_bancario("Pippo")
bancadeipoveri.crea_conto_bancario("Nino")
conto1=bancadeipoveri.crea_conto_bancario("Marco")

bancadeipoveri.get_conti_bancari()
bancadeipoveri.aggiungi_saldo_conto_bancario()
conto1.visualizza_saldo()
conto1.deposita(500)
bancadeipoveri.get_conti_bancari()

#cb=ContoBancario("Marco")
#cb.deposita(1200)
#cb.deposita(300)
#cb.preleva(1501)
#cb.visualizza_saldo()

        