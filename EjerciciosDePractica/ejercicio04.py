'''
Se desea realizar un programa en Python que permita ingresar n números enteros positivos y cuando se
Ingrese un numero negativo debe mostrar en pantalla el siguiente reporte.
a. Total de números ingresados
b. Total de números pares ingresados
c. Promedio de los números pares
d. Promedio de los números impares
e. Cuantos números son menores que 10
f. Cuantos números están entre 20 y 50
g. Cuantos números son mayores que 100
'''

totalNumerosIngresados = 0
numerosPares = 0
sumaNumerosPares = 0
numerosImpares = 0
sumaNumerosImpares = 0
menoresDe10 = 0
numerosEntre20y50 = 0
mayoresDe100 = 0

numeros = int(input("Escriba un número: "))

while numeros > 0:
    totalNumerosIngresados += 1

    if numeros % 2 == 0:
        numerosPares += 1
        sumaNumerosPares += numeros
    else:
        numerosImpares += 1
        sumaNumerosImpares += numeros

    if numeros < 10:
        menoresDe10 += 1
    elif 20 <= numeros <= 50:
        numerosEntre20y50 += 1
    elif numeros > 100:
        mayoresDe100 += 1

    numeros = int(input("Escriba un número: "))

promedioNumerosPares = sumaNumerosPares / numerosPares
promedioNumerosImpares = sumaNumerosImpares / numerosImpares

print(f"El total de números ingresados es: {totalNumerosIngresados}")
print(f"El total de números pares ingresados es: {numerosPares}")
print(f"El promedio de los números pares es: {promedioNumerosPares:.2f}")
print(f"El promedio de los números impares es: {promedioNumerosImpares:.2f}")
print(f"Números menores que 10: {menoresDe10}")
print(f"Números entre 20 y 50: {numerosEntre20y50}")
print(f"Números mayores que 100: {mayoresDe100}")
