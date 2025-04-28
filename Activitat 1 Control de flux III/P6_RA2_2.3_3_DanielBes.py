# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# mostra la taula de multiplicar d'un numero introduit per l'usuari
# Especificacions d'entrada:
# El numero
# ************************************************************

try:
    num = int(input("Introdueix un nombre enter: "))

    print(f"Taula de multiplicar del {num}:")
    
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

except ValueError:
    print("Error: Has d'introduir un nombre enter vàlid.")