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

estudiants = [Estudiant("Anna", 7), Estudiant("Marc", 4), Estudiant("Joan", 9)]
aprovats = [e.nom for e in estudiants if e.ha_aprovat()]
print("Han aprovat:", aprovats)