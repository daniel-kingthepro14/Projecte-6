# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Daniel Bes Guimera
# Data: 28/4/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# demana un nombre enter i imprimeix tots els nombres primers des de 2 fins a l'especificat
# Especificacions d'entrada:
# el nombre
# ************************************************************

def es_primer(n):
    """Comprova si un nombre és primer."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    num = int(input("Introdueix un nombre enter positiu: "))

    if num < 2:
        print("Error: Has d'introduir un nombre enter positiu més gran o igual a 2.")
    else:
        print(f"Nombres primers de 2 a {num}:")
        for i in range(2, num + 1):
            if es_primer(i):
                print(i)

except ValueError:
    print("Error: Has d'introduir un nombre enter vàlid.")