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

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu if preu > 0 else 0

    @property
    def preu(self):
        return self.__preu

    @preu.setter
    def preu(self, nou_preu):
        if nou_preu > 0:
            self.__preu = nou_preu
