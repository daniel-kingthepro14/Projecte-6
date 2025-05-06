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

class Joc:
    def __init__(self):
        self.__puntuacio = 0

    @property
    def puntuacio(self):
        return self.__puntuacio

    def sumar_punts(self, punts):
        if punts > 0:
            self.__puntuacio += punts

    def reiniciar_puntuacio(self):
        self.__puntuacio = 0
