# Diseña un programa que calcule el precio final de un articulo conociendo el precio inicial y el porcentaje de descuento.

precioInicial = float(input("Indique el valor del producto: "))
porcentajeDescuento = int(input("Escriba el porcentaje del descuento: "))
precioFinal = precioInicial*(1-porcentajeDescuento/100)
print(f'El precio a pagar por el artículo es: {precioFinal}')