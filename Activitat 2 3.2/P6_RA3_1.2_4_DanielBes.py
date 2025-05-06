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

class Usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya if len(contrasenya) >= 8 else None

    def canviar_contrasenya(self, nova_contrasenya):
        if len(nova_contrasenya) >= 8:
            self.__contrasenya = nova_contrasenya
            return "Contrasenya actualitzada."
        return "La contrasenya ha de tenir almenys 8 caràcters."

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau