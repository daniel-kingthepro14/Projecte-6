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

persones = [Persona("Pau", 28), Persona("Marta", 35), Persona("Joana", 42)]
for p in persones:
    if p.edat > 30:
        p.presentar_se()