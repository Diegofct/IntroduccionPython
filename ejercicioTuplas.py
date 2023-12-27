ventas = [
    ("ProductoA", 10, 150),
    ("ProductoB", 5, 200),
    ("ProductoA", 8, 120),
    ("ProductoC", 12, 80),
    ("ProductoB", 3, 210),
    ("ProductoA", 15, 130),
    ("ProductoC", 7, 85),
]

ventasTotalA=0
ventasTotalB=0
ventasTotalC=0

for producto in ventas:
    if producto[0]=="ProductoA":
        ventasTotalA += producto[1]
    if producto[0]=="ProductoB":
        ventasTotalB += producto[1]
    if producto[0]=="ProductoC":
        ventasTotalC += producto[1]


total_ventas = {"ProductoA": (ventasTotalA), "ProductoB": (ventasTotalB), "ProductoC": (ventasTotalC)}
print(total_ventas)

for clave, valor in total_ventas.items():
    if valor > 10:
        masVentas = {clave}
        print(f'Los productos que tuvieron más de 10 ventas son: {masVentas}')

print(f'Hola mundo')
        
