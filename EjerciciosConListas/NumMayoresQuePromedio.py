# Escriba un programa que pregunte al usuario cuántos datos ingresará, a continuación le pida que ingrese los datos uno por uno, y finalmente entregue como salida cuántos de los datos ingresados son mayores que el promedio.

cantidad_a_ingresar = int(input("Digite la cantidad de datos a ingresar: "))
listaDatos = []
contador = 0

for i in range(1, cantidad_a_ingresar + 1):
    datos = float(input(f'Escriba el dato {i}: '))
    listaDatos.append(datos)

cantidadDatos = len(listaDatos)
sumaDatos = sum(listaDatos)
promedioDatos = sumaDatos / cantidadDatos

for dato in listaDatos:
    if dato > promedioDatos:
        contador+=1

print(f'{contador} datos son mayores que el promedio')
