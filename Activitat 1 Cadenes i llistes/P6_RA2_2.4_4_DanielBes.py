# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 29/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Detecta si una paraula es un palíndrom
# Especificacions d'entrada:
# Una paraula
# ************************************************************

def es_palindrom(paraula):
    return paraula == paraula[::-1]

paraula = input("Introdueix una paraula: ").lower()
if es_palindrom(paraula):
    print(f'"{paraula}" és un palíndrom!')
else:
    print(f'"{paraula}" no és un palíndrom.')