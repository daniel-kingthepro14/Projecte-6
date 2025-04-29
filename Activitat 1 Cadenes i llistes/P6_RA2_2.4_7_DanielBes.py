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

cadena = input("Introdueix una cadena: ")
lletra = input("Introdueix la lletra que vols comptar: ")

if len(lletra) == 1:
    contador = cadena.count(lletra)
    print(f'La lletra "{lletra}" apareix {contador} vegades a la cadena.')
else:
    print("Si us plau, introdueix només una lletra.")
