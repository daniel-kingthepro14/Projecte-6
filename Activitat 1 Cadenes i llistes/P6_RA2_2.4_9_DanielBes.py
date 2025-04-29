# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 29/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Divideix una frase paraula per paraula
# Especificacions d'entrada:
# Una frase
# ************************************************************

frase = input("Introdueix una frase: ")

paraules = frase.split()

print("Les paraules de la frase són:")
for paraula in paraules:
    print(paraula)
