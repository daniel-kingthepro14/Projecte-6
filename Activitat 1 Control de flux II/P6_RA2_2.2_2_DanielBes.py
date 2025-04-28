# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Calcula la suma dels primers 100 numeros enters positius i mostra el resultat
# Especificacions d'entrada:
# 
# ************************************************************

suma = 0

for i in range(1, 101):
    suma += i

print("La suma dels primers 100 nombres enters és:", suma)