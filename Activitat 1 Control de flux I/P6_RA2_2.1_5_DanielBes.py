# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# 
# Especificacions d'entrada:
# 
# ************************************************************

from datetime import datetime

data_naixement = input("Introdueix la teva data de naixement (YYYY-MM-DD): ")

data_naixement = datetime.strptime(data_naixement, "%Y-%m-%d")

avui = datetime.today()
edat = avui.year - data_naixement.year - ((avui.month, avui.day) < (data_naixement.month, data_naixement.day))

print(f"Tens {edat} anys.")
print("Ets major d'edat." if edat > 18 else "No ets major d'edat.")