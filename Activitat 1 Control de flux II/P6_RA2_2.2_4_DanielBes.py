# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# Genera un numero entre 1 i 100 i l'usuari el te que endevinar, segons s'aproximi sortiran textos com "massa alt" o "massa baix"
# Especificacions d'entrada:
# Un numero
# ************************************************************

import random


num_secret = random.randint(1, 100)


print("Endevina el número entre 1 i 100!")


intent = None

while intent != num_secret:
    intent = int(input("Introdueix la teva resposta: "))
    
    if intent < num_secret:
        print("Massa baix! Intenta-ho de nou.")
    elif intent > num_secret:
        print("Massa alt! Intenta-ho de nou.")
    else:
        print("Felicitats! Has endevinat el número!")