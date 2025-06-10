# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 30/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# 
# Especificacions d'entrada:
# 
# ************************************************************

def multiplica_tot(*nombres):
    resultat = 1
    for nombre in nombres:
        resultat *= nombre
    return resultat

# 6. Multiplica una sèrie de nombres
print(multiplica_tot(2, 3, 4))
print(multiplica_tot(5, 10))