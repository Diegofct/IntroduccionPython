#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
numero = int(input("Digite un número: "))

# digito1 = numero // 100
# digito2 = (numero % 100) // 10
# digito3 = numero % 10

# numeroInverso = digito3*100 + digito2*10 + digito1
# print(f'El número con los dígitos en orden inverso es: {numeroInverso}')


#Escriba un programa que pida al usuario un entero de n dígitos, y entregue el número con los dígitos en orden inverso:

numeroStr = str(numero)
longitud = len(numeroStr)
numeroInverso = 0
for i in range(longitud):
    digito = numero % 10
    numero //= 10
    numeroInverso = numeroInverso*10+digito

print(f'El número con los dígitos en orden inverso es: {numeroInverso}')