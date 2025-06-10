try:
    with open("nombres.txt", "r", encoding="utf-8") as fitxer:
        for linia in fitxer:
            try:
                nombre = int(linia.strip())
                print(f"Nombre llegit: {nombre}")
            except ValueError:
                print(f"Error: '{linia.strip()}' no és un nombre enter vàlid.")
except FileNotFoundError:
    print("Error: El fitxer nombres.txt no existeix.")