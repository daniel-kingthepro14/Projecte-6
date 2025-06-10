# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Troba el numero maxim en una llista
# Especificacions d'entrada:
# 
# ************************************************************

def trobar_maxim(llista):
    maxim = llista[0]  # Inicialitzem el màxim amb el primer element
    for num in llista:
        if num > maxim:
            maxim = num
    return maxim

llista = [3, 7, 2, 9, 5, 10, 1]
print(f"El número màxim de la llista és: {trobar_maxim(llista)}")