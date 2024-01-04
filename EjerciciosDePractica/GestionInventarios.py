def registrar_producto(productos, codigo):
    if codigo in productos:
        print("¡Error! El código ya está en uso.")
        return

    nombre = input("Nombre del producto: ")
    valor_compra = float(input("Valor de compra del producto: "))
    valor_venta = float(input("Valor de venta del producto: "))
    stock_minimo = int(input("Stock mínimo permitido: "))
    stock_maximo = int(input("Stock máximo permitido: "))
    proveedor = input("Nombre del proveedor del producto: ")

    nuevo_producto = {
        'nombre': nombre,
        'valor_compra': valor_compra,
        'valor_venta': valor_venta,
        'stock_minimo': stock_minimo,
        'stock_maximo': stock_maximo,
        'proveedor': proveedor
    }

    productos[codigo] = nuevo_producto
    print(f"Producto {codigo} registrado correctamente.")

productos = {}

registrar_producto(productos, '001')
registrar_producto(productos, '002')

print("Diccionario de Productos:")
print(productos)


# def menu():
#     productos = []

#     while True:
#         print("\nMenú:")
#         print("1. Registrar Producto")
#         print("2. Visualizar Productos")
#         print("3. Actualizar Stock")
#         print("4. Informe de Productos Críticos")
#         print("5. Cálculo de Ganancia Potencial")
#         print("6. Salir")

#         opcion = input("Seleccione una opción (1-6): ")

#         if opcion == "1":
#             nuevo_producto = registrar_producto()
#             productos.append(nuevo_producto)
#             print(f"{nuevo_producto.nombre} ha sido registrado.")
#         elif opcion == "2":
#             visualizar_productos(productos)
#         elif opcion == "3":
#             actualizar_stock_producto(productos)
#         elif opcion == "4":
#             informe_productos_criticos(productos)
#         elif opcion == "5":
#             calcular_ganancia_potencial_total(productos)
#         elif opcion == "6":
#             print("Saliendo del programa. ¡Hasta luego!")
#             break
#         else:
#             print("Opción no válida. Inténtelo de nuevo.")

