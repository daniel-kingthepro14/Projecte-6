# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 29/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Retorna la llista al reves
# Especificacions d'entrada:
# 
# ************************************************************

def invertir_llista(llista):
    return llista[::-1]

llista = [1, 2, 3, 4, 5]
llista_invertida = invertir_llista(llista)
print("Llista invertida:", llista_invertida)