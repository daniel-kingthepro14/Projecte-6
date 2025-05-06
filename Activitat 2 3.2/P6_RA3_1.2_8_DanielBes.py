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

class Alumne:
    def __init__(self, edat=0):
        self.__edat = edat if edat >= 0 else 0

    @property
    def edat(self):
        return self.__edat

    @edat.setter
    def edat(self, nova_edat):
        if nova_edat >= 0:
            self.__edat = nova_edat
