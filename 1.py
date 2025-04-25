# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data:25/4/2025

# Versió: 1.0

# Descripció:

# Especificacions d'entrada: El radi del cercle

import math

PI = 3.1416 # constant

def calcular_area(radi):
    return PI * radi ** 2

radi = float(input("Introdueix el radi: "))

area = calcular_area(radi)
print("L'area del cercle és:", area)

# ● Quines són les constants?

# Les constans son: PI

# ● Quines són les variables?

# Les variables son: radi i area

# ● Quina part és una funció?

# def calcular_area(radi):
#     return PI * radi ** 2

# ● Quina línia llegeix dades de l’usuari?

# radi = float(input("Introdueix el radi: "))

# ● Quina línia mostra el resultat?

# print("L'area del cercle és:", area)