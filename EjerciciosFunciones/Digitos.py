# Escriba un programa que determine la cantidad de dígitos en un número entero ingresado por el usuario:

def pedir_numero():
    numero = int(input("Ingrese un número: "))
    return numero

def calcular_digitos(numero):
    digitos = len(str(numero))
    return digitos

num = pedir_numero()
print(num)

calcularDigitos = calcular_digitos(num)
print(f'La cantidad de dígitos para el número {num} es de {calcularDigitos} dígitos')