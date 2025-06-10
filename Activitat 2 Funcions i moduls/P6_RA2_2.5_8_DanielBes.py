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

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
    # 8. Calcula factorials de diversos nombres
print(factorial(0))
print(factorial(3))
print(factorial(5))