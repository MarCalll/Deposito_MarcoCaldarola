class Libro:
    def __init__(self, titolo,autore,pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    def descrizione(self):
        print("Il libro", self.titolo, "è stato scritto da", self.autore, "e ha",self.pagine,"pagine.")
    
#lib1=Libro("Il vecchio e il mare","Ernest Hemingway",204)
#lib2=Libro("Il cuore rivelatore","Edgar Allan Poe",21)

#lib1.descrizione()
#lib2.descrizione()