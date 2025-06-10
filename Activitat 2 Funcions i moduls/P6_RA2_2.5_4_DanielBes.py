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

def es_parell(numero):
    return numero % 2 == 0

# 4. Comprova si diferents nombres són parells
for numero in [1, 2, 3, 4, 5, 6]:
    print(f"El número {numero} és parell: {es_parell(numero)}")