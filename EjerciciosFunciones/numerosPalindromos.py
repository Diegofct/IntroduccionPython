def invertir_numero(numero):
    numeroStr = str(numero)
    longitud = len(numeroStr)
    sliced_str = numeroStr[::-1]
    return int(sliced_str)

num = int(input("Escriba un número de mas de dos dígitos: "))

if num == invertir_numero(num):
    print(f'{num} es palíndromo')
else:
    print(f'{num} no es palíndromo')