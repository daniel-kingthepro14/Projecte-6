# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 29/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Demana 10 numeros i crea 2 llistes una amb parells i una amb senars
# Especificacions d'entrada:
# Numero
# ************************************************************

parells = []
senars = []

for i in range(10):
    numero = int(input(f"Introdueix el número {i+1}: "))
    
    if numero % 2 == 0:
        parells.append(numero)
    else:
        senars.append(numero)

print("Nombres parells:", parells)
print("Nombres senars:", senars)
