import math

numeros_reales = [1.5, 9.5]

def desviacion_estandar(valores):
    n = len(valores)
    x = sum(valores)
    promedio = x/n
    xi = [valor for valor in valores]

    desviacion = math.sqrt(sum((xi - promedio) ** 2 for xi in valores) / (n - 1))
    return desviacion

resultado = desviacion_estandar(numeros_reales)
print(resultado)