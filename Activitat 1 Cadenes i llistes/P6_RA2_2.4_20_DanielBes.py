# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 29/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# demana una llista de paraules i crea una nova llista amb nomes les paraules que començen per una vocal
# Especificacions d'entrada:
# Una llista de paraules separades amb espais
# ************************************************************

paraules = input("Introdueix una llista de paraules separades per espais: ").split()

vocals = "aeiouAEIOU"

paraules_vocals = [paraula for paraula in paraules if paraula[0] in vocals]

print("Paraules que comencen per vocal:", paraules_vocals)
