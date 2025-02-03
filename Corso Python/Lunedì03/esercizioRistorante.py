class Ristorante:
    operativo=False
    menu=[]
    
    def __init__(self, nome,t_cucina):
        self.nome = nome
        self.t_cucina = t_cucina
    
    def descrivi_ristorante(self):
        print("Ristorante chiamato:",self.nome,"con tipo di cucina:",self.t_cucina)
        
    def stato_apertura(self):
        if self.operativo==True:
            print("il ristorante è aperto")
        else:
            print("il ristorante è chiuso")
            
    def apri_ristorante(self):
        self.operativo=True
        self.stato_apertura()
        
    def chiudi_ristorante(self):
        self.operativo=False
        self.stato_apertura()
        
    def aggiungi_al_menu(self,nome_piatto):
        self.menu.append(nome_piatto)
    
    def rimuovi_dal_menu(self,nome_piatto):
        for ele in self.menu:
            print(ele)
            if ele==nome_piatto:
                self.menu.remove(nome_piatto)
                

    def stampa_menu(self):
        print(self.menu)

ris1=Ristorante("Da Luigi","Vegana")

ris1.descrivi_ristorante()
ris1.stato_apertura()
#ris1.apri_ristorante()
#ris1.chiudi_ristorante()
ris1.aggiungi_al_menu("Lasagna")
ris1.aggiungi_al_menu("Lasagna1")
ris1.aggiungi_al_menu("Lasagna2")
ris1.aggiungi_al_menu("Lasagna3")
ris1.rimuovi_dal_menu("Lasagna2")
ris1.stampa_menu()
        