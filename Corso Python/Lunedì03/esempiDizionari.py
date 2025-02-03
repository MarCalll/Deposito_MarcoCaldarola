studente = {
    "nome":"alice",
    "età":20,
    "sesso":"Femmina"
    }

print(studente)
print(studente["nome"])
print(studente["età"])
studente["città"]="Roma"
print(studente)
print(studente.keys())
print(studente.values())
print(studente.get("nome"))