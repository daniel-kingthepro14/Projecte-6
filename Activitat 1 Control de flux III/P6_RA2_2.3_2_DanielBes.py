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
    num = int(input("Introdueix un nombre enter: "))

    suma = sum(range(1, num + 1))

    print(f"La suma dels nombres de 1 a {num} és {suma}")

except ValueError:
    print("Error: Has d'introduir un nombre enter vàlid.")
