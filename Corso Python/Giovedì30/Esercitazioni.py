#2
numeri_primi = []

def decoratore_per_numeri_primi(funzione):
    def wrapper(*args,**kwargs):
        while True:
            risultato = funzione(*args, **kwargs)
            if risultato == True:
                numeri_primi.append(args[0])
                print("si")
                args = (int(input("Scegli un altro numero: ")),)
            else:
                break
            
    return wrapper

@decoratore_per_numeri_primi
def primo_o_no(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

nome=input("Come ti chiami")
numero=int(input("Scegli un numero"))

numeri_primi.append(nome)
primo_o_no(numero)
print("Numeri primi trovati:", numeri_primi)