import libro
class Libreria:
    catalogo=[]
    def aggiungi_libro(self,libro):
        self.catalogo.append({"autore":libro.autore,"titolo":libro.titolo,"isbn":libro.isbn,"oggetto":libro})
    
    def mostra_catalogo(self):
        print("Libri nel catalogo:")
        for ele in self.catalogo:
            print(ele['oggetto'].descrizione())
            
    def cerca_per_titolo(self,titolo):
        print("Ricerca titoli nel catalogo:")
        for ele in self.catalogo:
            if ele['titolo']==titolo:
                print(ele['oggetto'].descrizione())
            
    def rimuovi_libro(self,isbn):
        for ele in self.catalogo:
            if ele['isbn']==isbn:
                self.catalogo.remove(ele)
            
mio1 = libro.Libro("Il cuore rivelatore","Edgar Allan Poe")
mio2 = libro.Libro("Il vecchio e il mare","Ernest Hemingway")
mio3 = libro.Libro("Uno, nessuno e centomila","Luigi Pirandello")
lib = Libreria()
lib.aggiungi_libro(mio1)
lib.aggiungi_libro(mio2)
lib.aggiungi_libro(mio3)
lib.rimuovi_libro(1337)
lib.mostra_catalogo()
lib.cerca_per_titolo('titolo2')