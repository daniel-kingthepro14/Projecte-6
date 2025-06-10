# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 30/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# 
# Especificacions d'entrada:
# 
# ************************************************************

def estat_persona(edat):
    if edat < 18:
        return "Menor d'edat", "Encara no és adult"
    elif edat < 65:
        return "Adult", "Persona en edat activa"
    else:
        return "Jubilat", "Persona retirada"
    
    # 9. Determina l'estat de diferents edats
for edat in [12, 25, 70]:
    estat, descripcio = estat_persona(edat)
    print(f"Edat: {edat}, Estat: {estat}, Descripció: {descripcio}")