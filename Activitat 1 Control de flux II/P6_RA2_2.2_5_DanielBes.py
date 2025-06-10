# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 
# Versió: 1.0
# ************************************************************
# Descripció:
# 
# Especificacions d'entrada:
# 
# ************************************************************

num = int(input("Introdueix un número enter positiu: "))


if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} no és un nombre primer.")
            break
    else:
        print(f"{num} és un nombre primer.")
else:
    print("El número ha de ser més gran que 1!")