# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 29/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Elimina els duplicats d'una llista
# Especificacions d'entrada:
# 
# ************************************************************

def elimina_duplicats(llista):
    return list(set(llista))

# Exemple d'ús
llista = [3, 7, 3, 12, 7, 9, 12, 5, 9]
llista_sense_duplicats = elimina_duplicats(llista)
print("Llista sense duplicats:", llista_sense_duplicats)