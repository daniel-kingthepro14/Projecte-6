# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 9/5/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# 
# Especificacions d'entrada:
# 
# ************************************************************

class Animal:
    def parlar(self):
        pass  # Mètode abstracte

class Gos(Animal):
    def parlar(self):
        print("Bup bup!")

class Gat(Animal):
    def parlar(self):
        print("Miau!")

# Crida del mètode parlar()
gos = Gos()
gat = Gat()

gos.parlar()
gat.parlar()