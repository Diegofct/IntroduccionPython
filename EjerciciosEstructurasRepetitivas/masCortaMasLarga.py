n = int(input("Digite la cantidad de palabras que va a escribir: "))

palabraMasLarga = ""
palabraMasCorta = None

for i in range (n):
    palabras = input("Escriba una palabra cualquiera: ")

    if len(palabras) > len(palabraMasLarga):
        palabraMasLarga = palabras

    if palabraMasCorta is None or len(palabras) < len(palabraMasCorta):
        palabraMasCorta = palabras

print(f"La palabra más larga es: {palabraMasLarga}")
print(f"La palabra más corta es: {palabraMasCorta}") 