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

def filtra_parells(llista):
    return [num for num in llista if es_parell(num)]

# 10. Filtra nombres parells de diverses llistes
print(filtra_parells([1, 2, 3, 4, 5, 6]))
print(filtra_parells([10, 15, 20, 25, 30]))