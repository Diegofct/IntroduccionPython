#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras.

import math

catetoA = float(input("Digite el valor para el cateto A: "))
catetoB = float(input("Digite el valor para el cateto B: "))

hipotenusa = math.sqrt(math.pow(catetoA,2)+math.pow(catetoB,2))
print(f'El valor de la hipotenusa es: {hipotenusa}')