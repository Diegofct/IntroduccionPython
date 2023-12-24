#Escriba un programa que pregunte al usuario cuántos datos ingresará, a continuación le pida que ingrese los datos uno por uno, y finalmente entregue como salida cuántos de los datos ingresados son mayores que el promedio.

cantidad_ingresar = int(input("Digite la cantidad de datos a ingresar: "))
lista = []
promedio = 0

for i in range(cantidad_ingresar):
    escribir_dato = float(input(f'Escriba el dato {i+1}: '))
    lista.append(escribir_dato)

promedio = sum(lista)/cantidad_ingresar
print(f'El promedio de los datos ingresados es: {promedio}')

mayores_que_promedio = sum(1 for numero in lista if numero>promedio)
print(f"La cantidad de datos mayores que el promedio es de: {mayores_que_promedio}")






    