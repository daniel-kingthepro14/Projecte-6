# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 29/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# 
# Especificacions d'entrada:
# 
# ************************************************************

def elimina_espais(cadena):
    return cadena.replace(" ", "")

text = input("Introdueix una cadena: ")
text_sense_espais = elimina_espais(text)
print("Cadena sense espais:", text_sense_espais)