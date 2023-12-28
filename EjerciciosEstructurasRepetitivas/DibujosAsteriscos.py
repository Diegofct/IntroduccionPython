#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos: Altura 3, ancho 5

altura = int(input("Digite la altura del rectángulo: "))
ancho = int(input("Digite el ancho del rectángulo: "))

for i in range(altura):
    for j in range(ancho):
        print("*", end=" ")
    print()