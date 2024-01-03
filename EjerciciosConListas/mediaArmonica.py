# La media armónica de un conjunto de datos es el recíproco de la suma de los recíprocos de los datos, multiplicada por la cantidad de datos:

def media_armonica(datos):
    if not datos:
        raise ValueError("La lista de datos no puede estar vacía.")

    suma_inversos = sum(1 / x for x in datos)
    media_arm = len(datos) / suma_inversos
    return media_arm

datos = [6, 1, 4, 8]
resultado = media_armonica(datos)
print(f"La media armónica de los datos es: {resultado}")

