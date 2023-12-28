#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.

pulgada = 2.54
centimetros = float(input("Ingrese el valor en centímetros: "))

convertir = round(centimetros/pulgada,2)
print(f'{centimetros} cm es igual a {convertir} pulgadas')