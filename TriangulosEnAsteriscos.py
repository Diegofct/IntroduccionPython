#Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo: altura 5

altura = int(input("Ingrese la altura del triángulo: "))

for i in range(1, altura + 1):
    # Imprime espacios en blanco para alinear el triángulo
    print(" " * (altura - i), end="")

    # Imprime asteriscos para cada fila
    print("* " * i)



