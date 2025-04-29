# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 29/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Mostra la primera i ultima lletra d'una cadena de caracters
# Especificacions d'entrada:
# Una cadena
# ************************************************************

cadena = input("Introdueix una cadena: ")

if cadena:
    print("Primera lletra:", cadena[0])
    print("Última lletra:", cadena[-1])
else:
    print("Has introduït una cadena buida.")
