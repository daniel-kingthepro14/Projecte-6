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

compte = CompteBancari()
compte.ingressar(100)
compte.retirar(30)
compte.retirar(100)  # saldo insuficient
compte.veure_saldo()