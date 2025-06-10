with open("sortida.txt", "r+", encoding="utf-8") as fitxer:
    print(fitxer.read())  # Llegeix el contingut existent
    fitxer.write("\nLínia afegida")