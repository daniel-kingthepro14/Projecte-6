# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# imprimeix tots els nombres parells fins al nombre introduit per l'usuari
# Especificacions d'entrada:
# el nombre
# ************************************************************

try:
    num = int(input("Introdueix un nombre enter positiu: "))

    if num < 0:
        print("Error: Has d'introduir un nombre enter positiu.")
    else:
        print(f"Nombres parells de 0 a {num}:")
        for i in range(0, num + 1, 2):
            print(i)

except ValueError:
    print("Error: Has d'introduir un nombre enter vàlid.")