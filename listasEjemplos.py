'''
nombres = ["Camilo", "Juan", "Pedro", "Mario", "Jose"]
nuevos_nombres = [name for name in nombres if len(name)>5]
print(nuevos_nombres)
'''

def suma_elementos(lista):
    return sum(lista)

lista_numeros = [1, 2, 3, 4, 5]
print(suma_elementos(lista_numeros))  # Salida esperada: 15

def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(filtrar_pares(lista_numeros))  # Salida esperada: [2, 4, 6, 8]

def es_palindromo(palabra):
    return palabra == palabra[::-1]

palabra = "radar"
print(es_palindromo(palabra))  # Salida esperada: True

def unir_listas(lista1, lista2):
    return lista1 + lista2

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(unir_listas(lista1, lista2))  # Salida esperada: [1, 2, 3, 4, 5, 6]

def contar_elementos(lista):
    contador = {}
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    return contador

lista = [1, 2, 3, 1, 2, 4, 5, 1, 2]
print(contar_elementos(lista))  # Salida esperada: {1: 3, 2: 3, 3: 1, 4: 1, 5: 1}

