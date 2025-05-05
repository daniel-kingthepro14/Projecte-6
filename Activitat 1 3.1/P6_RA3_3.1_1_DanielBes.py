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

class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_info(self):
        print(f"{self.marca} {self.model}, {self.any}")