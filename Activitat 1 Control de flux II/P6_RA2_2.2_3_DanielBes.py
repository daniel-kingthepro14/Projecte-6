# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# demana un numero i mostra la seva taula de multiplicar
# Especificacions d'entrada:
# Un numero
# ************************************************************


num = int(input("Introdueix un número enter: "))

print(f"Taula de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")