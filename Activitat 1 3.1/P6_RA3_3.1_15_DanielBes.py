# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 5/5/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# 
# Especificacions d'entrada:
# 
# ************************************************************

def aplicar_descompte10(productes):
    for p in productes:
        p.aplicar_descompte(10)

productes = [Producte("Llibre", 20), Producte("Bolígraf", 2)]
aplicar_descompte10(productes)
for p in productes:
    print(f"{p.nom}: {p.preu:.2f}€")