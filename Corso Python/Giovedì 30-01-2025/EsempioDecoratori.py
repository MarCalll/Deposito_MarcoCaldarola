
def decoratore(pippo):
    def wrapper():
        print("prima dell'esecizopne della funzione")
        pippo()
        print("Dopo l'esecuzione della funzone")
    return wrapper

@decoratore
def saluta():
    print("Ciao!")
    
# saluta()

def decoratore_con_argomenti(funzione):
    def wrapper(*args,**kwargs):
        print("prima")
        risultato=funzione(*args,**kwargs)
        print("dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a,b):
    return a+b

print(somma(3,4))

def logger(funzione):
    def wrapper(*args, **kwargs):
        print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
        risultato = funzione(*args, **kwargs)
        print(f"Risultato di {funzione.__name__}: {risultato}")
        return risultato
    return wrapper

@logger
def moltiplica(a, b):
    return a * b

# Chiamata alla funzione decorata
moltiplica(3, 4)