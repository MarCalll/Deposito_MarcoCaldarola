import random
class Libro:
    isbn_generati = set()  # Set per tenere traccia degli ISBN già usati
    def __init__(self, titolo,autore):
        self.titolo = titolo
        self.autore = autore
        self.isbn = self.generaISBN()
    
    @classmethod
    def generaISBN(cls):
        while True:
            nuovo_isbn = random.randint(1000, 9999)
            if nuovo_isbn not in cls.isbn_generati:
                cls.isbn_generati.add(nuovo_isbn)
                return nuovo_isbn
        
    def descrizione(self):
        return f'"{self.titolo}" scritto da {self.autore}, codice ISBN: {self.isbn}'
    
#mio = Libro("titolo","autore",1337)
#print(mio.descrizione())