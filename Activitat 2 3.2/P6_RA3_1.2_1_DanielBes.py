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

class CompteBancari:
    def __init__(self, saldo=0):
        self.__saldo = saldo

    def ingressar(self, q):
        if q > 0: self.__saldo += q

    def retirar(self, q):
        if 0 < q <= self.__saldo: self.__saldo -= q

    def saldo(self):
        return self.__saldo