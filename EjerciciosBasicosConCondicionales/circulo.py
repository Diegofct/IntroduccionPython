#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área
#Perímetro = 2(pi) por radio. 
#Área = pi por radio al cuadrado.
import math

radio = float(input("Ingrese el valor del radio del circulo: "))

perimetro = round(2*math.pi*radio, 2)
print(f'El perímetro del círculo con radio {radio} es: {perimetro}')

area = round(math.pi*math.pow(radio,2),2)

print(f'El área del círuclo con radio {radio} es: {area}')
