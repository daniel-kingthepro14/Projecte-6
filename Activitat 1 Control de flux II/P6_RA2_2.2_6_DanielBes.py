# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Mostra els 10 primers nombres de la sequencia de Fibonacci
# Especificacions d'entrada:
# 
# ************************************************************

a, b = 0, 1


for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b