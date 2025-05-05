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

cercles = [Cercle(3), Cercle(5), Cercle(6)]
for c in cercles:
    if c.area() > 50:
        print(f"Cercle de radi {c.radi} té àrea {c.area():.2f} > 50")