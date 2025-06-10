import os

if os.path.exists("dades.txt"):
    with open("dades.txt", "r", encoding="utf-8") as fitxer:
        print(fitxer.read())
else:
    print("Error: El fitxer dades.txt no existeix.")