# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Diferencia entre si un numero es mes gran o no que zero
# Especificacions d'entrada:
# Numero especificat per l'usuari
# ************************************************************

print('Insereix un numero')
num = int(input())

if num < 0:
    print('El numero es mes petit que zero')
else: print('El numero es mes gran que zero')