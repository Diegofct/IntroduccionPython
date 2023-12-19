import math

numeros_reales = [1.3, 1.3, 1.3]
n = len(numeros_reales)
x = sum(numeros_reales)
promedio = x/n
xi = [valores for valores in numeros_reales]


def desviacion_estandar(valores):
    dv = (math.sqrt(x*(xi-promedio/(n-1))))
    return dv

desviacion_estandar()