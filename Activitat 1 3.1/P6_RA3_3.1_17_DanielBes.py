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

class Gos(Animal):
    def fer_soroll(self):
        print("Bup bup!")

gos = Gos("Rocky", "Gos")
gos.fer_soroll()