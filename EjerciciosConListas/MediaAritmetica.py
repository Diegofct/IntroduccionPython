datos = []

def media_aritmetica(datos):
    sumaDatos = sum(datos)
    cantidadDatos = len(datos)
    media = sumaDatos / cantidadDatos
    return media

def ingresar_datos_lista():
    cantidadDatos = int(input("Digite la cantidad de datos a ingresar: "))
    for i in range(1, cantidadDatos+1):
        añadirDatos = int(input(f"Ingrese el dato {i}: "))
        datos.append(añadirDatos)
    return datos
    
promedio = media_aritmetica(ingresar_datos_lista())
print(f"La media arimética de la lista es: {promedio}")


