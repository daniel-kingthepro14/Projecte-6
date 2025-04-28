# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Demana un numro entre 1 i 10 i retorna aprovat o suspes
# Especificacions d'entrada:
# La nota (numero)
# ************************************************************

nota = int(input("Introdueix la teva nota (1-10): "))

if nota > 5:
    print("Aprovat")
else:
    print("Suspès")