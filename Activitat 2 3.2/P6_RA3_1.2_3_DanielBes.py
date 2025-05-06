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

class Termostat:
    def __init__(self, temperatura=20):
        self.__temperatura = temperatura if 10 <= temperatura <= 30 else 20

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nova_temperatura):
        if 10 <= nova_temperatura <= 30:
            self.__temperatura = nova_temperatura
