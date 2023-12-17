#Parte 1, ejercicio 11:
#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:

# numero1 = int(input("Digite un número: "))
# numero2 = int(input("Digite otro número: "))

# print(f'Los número se mostrarán ordenados de menor a mayor')

# if numero1<numero2 :
#     print(f'{numero1} - {numero2}')
# elif numero2<numero1 : 
#     print(f'{numero2} - {numero1}')


#Parte 2, ejercicio 11
#A continuación, escriba otro programa que haga lo mismo con tres números:
num1 = int(input("Digite el primer número: "))
num2 = int(input("Digite el segundo número: "))
num3 = int(input("Digite el tercer número: "))

numeros_ordenados = sorted([num1, num2, num3])
print("Números ordenados de menor a mayor:", numeros_ordenados)
