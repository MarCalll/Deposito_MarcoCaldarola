#Variabile globale
numero=10

def funzione_esterna():
    #variabile locale nella funzione esterna
    numero=5

    
    def funzione_interna():
        #utilizzo nonlocal per modificare la bariabile locale della funzione esterna nonlocal numero
        numero=3
        print("numero dentro funzione_interna(nonlocal):",numero)
        
    funzione_interna()
    print("numero dentro funzione_esterna (locale):",numero)
    
print("numero nel main globale",numero)
funzione_esterna()
print("numero nel main dopo chiamata (globale non cambiato):",numero)
