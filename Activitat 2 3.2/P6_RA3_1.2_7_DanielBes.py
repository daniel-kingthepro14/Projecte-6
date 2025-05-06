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

class Rellotge:
    def __init__(self, hores=0):
        self.__hores = hores if 0 <= hores <= 23 else 0

    @property
    def hores(self):
        return self.__hores

    @hores.setter
    def hores(self, noves_hores):
        if 0 <= noves_hores <= 23:
            self.__hores = noves_hores

    def mostrar_hora(self):
        return f"{self.__hores:02d}:00"