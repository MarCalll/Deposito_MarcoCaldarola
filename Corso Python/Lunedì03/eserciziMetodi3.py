import eserciziMetodi2
class Biblioteca:
    #permette di creare un libro e stamparlo
    libri=[]
    
    def creaLibro(self,titolo,autore,pagine):
        nuovoLibro= eserciziMetodi2.Libro(titolo,autore,pagine)
        self.libri.append(nuovoLibro)
         
    def stampaLibri(self):
        for libro in self.libri:
            print(libro.autore, libro.titolo,libro.pagine)
            
bib1=Biblioteca()

bib1.creaLibro("Il vecchio e il mare","Ernest Hemingway",204)
bib1.creaLibro("Il cuore rivelatore","Edgar Allan Poe",21)
bib1.stampaLibri()
