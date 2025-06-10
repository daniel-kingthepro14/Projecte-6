# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# deferencia entre les vocals i indica si la lletra introduida es una vocal o consonant
# Especificacions d'entrada:
# La lletra
# ************************************************************

lletra = input("Introdueix una lletra: ").lower()

if lletra in "aeiou":
    print("És una vocal.")
elif lletra.isalpha():
    print("És una consonant.")
else:
    print("No has introduït una lletra.")