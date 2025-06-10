try:
    with open("resultats.txt", "w", encoding="utf-8") as fitxer:
        fitxer.write("Resultats de l'experiment")
except PermissionError:
    print("Error: No tens permisos per escriure en el fitxer.")