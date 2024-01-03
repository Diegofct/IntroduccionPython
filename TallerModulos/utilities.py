def validacionNumerica(numero):
    while True:
        dato=input(numero)
        if dato.isdigit():
            return int(dato)
            break
        else:
            print(f"Error, el dato no es numérico")

def ingresarDatoCadena(texto):
    while True:
        cadena = input(texto)
        if cadena.isdigit():
            print(f"Error, se necesita ingresar una cadena de texto o string")
        else:
            return cadena

def ingresarDatoPositivo(numero):
    while True:
        dato = input(numero)
        if dato.isdigit() and int(dato) > 0:
            return int(dato)
        elif dato[0] == "-" and dato[1:].isdigit():
            print("Por favor, ingrese un número positivo.")
        else:
            print("Error, el dato no es un valor numérico.")


            


