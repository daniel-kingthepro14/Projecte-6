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

class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * self.radi ** 2

    def perimetre(self):
        return 2 * math.pi * self.radi