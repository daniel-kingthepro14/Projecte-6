# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 29/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Compta les vocals en una frase
# Especificacions d'entrada:
# Una frase introduida per l'usuari
# ************************************************************


frase = input("Introdueix una frase: ")

vocals = "aeiouAEIOU"

contador = sum(1 for lletra in frase if lletra in vocals)

print("La frase conté", contador, "vocals.")
