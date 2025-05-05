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

class Biblioteca:
    def __init__(self):
        self.llibres = []

    def afegir_llibre(self, llibre):
        self.llibres.append(llibre)

    def mostrar_llibres(self):
        for llibre in self.llibres:
            llibre.mostrar_info()

biblio = Biblioteca()
biblio.afegir_llibre(Llibre("1984", "George Orwell", 1949))
biblio.afegir_llibre(Llibre("La plaça del Diamant", "Mercè Rodoreda", 1962))
biblio.mostrar_llibres()