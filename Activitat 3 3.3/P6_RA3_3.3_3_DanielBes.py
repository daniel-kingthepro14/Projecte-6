# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 9/5/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# 
# Especificacions d'entrada:
# Carret de compra i descompte: Calcula el total amb un descompte aplicable.
# ************************************************************

class Descompte20:
    def aplicar(self, total):
        return total * 0.2  # Aplica un descompte del 20%

class CarretCompra:
    def __init__(self, total, descompte):
        self.total = total
        self.descompte = descompte  # Dependència injectada

    def calcular_total_amb_descompte(self):
        descompte_aplicat = self.descompte.aplicar(self.total)
        return self.total - descompte_aplicat

# Ús del nou sistema de descompte
descompte20 = Descompte20()
carret = CarretCompra(100, descompte20)
print(carret.calcular_total_amb_descompte())
