# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 29/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Demana 5 paraules a l'usuari les emmagatzema en una llista
# Especificacions d'entrada:
# 
# ************************************************************

paraules = []

for i in range(5):
    paraula = input(f"Introdueix la paraula {i+1}: ")
    paraules.append(paraula)

print("Llista de paraules:", paraules)