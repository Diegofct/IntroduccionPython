def media_aritmetica(lista):
    sumaDatos = sum(lista)
    cantidadDatos = len(lista)
    media = sumaDatos / cantidadDatos
    return media

def ingresar_datos_lista():
    datos = []
    cantidadDatos = int(input("Digite la cantidad de datos a ingresar: "))
    for i in range(1, cantidadDatos+1):
        añadirDatos = int(input(f"Ingrese el dato {i}: "))
        datos.append(añadirDatos)
    return datos
    
promedio = media_aritmetica(ingresar_datos_lista())
print(f"La media aritmética de la lista es: {promedio}")



