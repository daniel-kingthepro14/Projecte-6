# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 29/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Substitueix les lletres a per @ en la frase
# Especificacions d'entrada:
# Una frase
# ************************************************************


frase = input("Introdueix una frase: ")

frase_modificada = frase.replace("a", "@").replace("A", "@")

print("Frase modificada:", frase_modificada)