try:
    fitxer = open("error_fitxer.txt", "r", encoding="utf-8")
    contingut = fitxer.read()
    print(contingut)
finally:
    fitxer.close()
    print("El fitxer s'ha tancat correctament.")