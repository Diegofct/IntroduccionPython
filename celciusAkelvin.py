'''
Diseñar un programa que convierta un dato de temperatura celcius a kelvin.
k=c+273.15 el dato será proporcionado por el usuario.
'''
gradosCelcius = float(input("Escriba el valor de la temperatura en celcius: "))
kelvin = gradosCelcius + 273.15
print(f'El resultado es: {kelvin}k')