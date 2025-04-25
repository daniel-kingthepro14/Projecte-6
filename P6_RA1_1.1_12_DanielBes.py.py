# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data:24/4/2025

# Versió: 1.0

# Descripció: Calcula l'area d'un cercle a partir del radi

# Especificacions d'entrada: El valor del radi


# Area = PI * R2

PI = 3.1416
print('Introdueix un valor per al radi')

radi = int(input())

area = PI *(radi ** 2)

print('Larea del cercle es:', area)