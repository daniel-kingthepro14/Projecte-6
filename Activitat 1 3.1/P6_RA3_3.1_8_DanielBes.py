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

class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    def fer_soroll(self):
        print("Fa un soroll")