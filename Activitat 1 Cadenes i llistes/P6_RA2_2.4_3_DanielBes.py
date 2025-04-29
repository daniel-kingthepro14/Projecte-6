# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 29/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Reverteix la cadena de caracters
# Especificacions d'entrada:
# Una cadena de caracters
# ************************************************************

def revertir_cadena(cadena):
    return cadena[::-1]

text = input("Introdueix una cadena: ")
text_revertit = revertir_cadena(text)
print("Cadena revertida:", text_revertit)