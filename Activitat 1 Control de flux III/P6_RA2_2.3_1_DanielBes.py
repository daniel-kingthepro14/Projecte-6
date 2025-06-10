# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# 
# Especificacions d'entrada:
# 
# ************************************************************

try:
    # Demana a l'usuari que introdueixi un nombre enter
    num = int(input("Introdueix un nombre enter: "))

    # Genera la seqüència de nombres amb range()
    for i in range(num + 1):
        print(i)

except ValueError:
    print("Error: Has d'introduir un nombre enter vàlid.")
