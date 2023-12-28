print("Potencia\tFraccion\tSuma")

potencia = 1
fraccion = 0.5
suma = 0

while fraccion > 0.000001:
    print(f"{potencia}\t\t{fraccion}\t\t{suma + fraccion}")
    suma += fraccion
    fraccion /= 2
    potencia += 1
