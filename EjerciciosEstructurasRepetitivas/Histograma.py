#Escriba un programa que pida al usuario que ingrese varios valores enteros, que pueden ser positivos o negativos. Cuando se ingrese un cero, el programa debe terminar y mostrar un gráfico de cuántos valores positivos y negativos fueron ingresados:

contarPositivos = 0
contarNegativos = 0

while True:
    valores = int(input("Digite un valor, puede ser positivo o negativo, ingrese 0 para terminar: "))
    if valores < 0:
        contarNegativos+=1
    elif valores > 0:
        contarPositivos+=1
    elif valores == 0:
        break


print(f'Cantidad que ingresó de valores positivos: {contarPositivos}')
print(f'Cantidad que ingresó de valores negativos: {contarNegativos}')
        