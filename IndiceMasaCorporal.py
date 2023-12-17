#El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.
#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.

import math

edad = int(input("Digite la edad: "))
peso = float(input("Digite el peso en kg: "))
estatura = float(input("Digite la estatura en metros: "))

imc = peso/(math.pow(estatura,2))

if imc<18.5 :
    print(f'Tiene un nivel bajo de peso')
elif imc>=18.5 and imc<=24.9 :
    print(f'Tiene un nivel de peso normal')
elif imc>=20.5 and imc <=29.9 :
    print(f'Tiene un nivel de sobre peso')
else:
    print(f'Tiene un nivel de obesidad')