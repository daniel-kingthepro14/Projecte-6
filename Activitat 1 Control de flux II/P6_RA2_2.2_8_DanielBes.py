# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Mostra la quantitat de vocals en una frase
# Especificacions d'entrada:
# Una frase
# ************************************************************

def comptar_vocals(frase):
    vocals = "aeiouAEIOU"
    comptador = 0
    for lletra in frase:
        if lletra in vocals:
            comptador += 1
    return comptador

frase = input("Escriu una frase: ")
num_vocals = comptar_vocals(frase)
print(f"La frase conté {num_vocals} vocals.")
