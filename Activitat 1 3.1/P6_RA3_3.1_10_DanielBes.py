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

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre_punt):
        return math.sqrt((self.x - altre_punt.x)**2 + (self.y - altre_punt.y)**2)