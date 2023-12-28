#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.

palabra1 = input("Escriba una palabra: ")
palabra2 = input("Escriba otra palabra: ")

cantidad1 = len(palabra1)
cantidad2 = len(palabra2)

if cantidad1 > cantidad2:
    diferencia = cantidad1 - cantidad2
    print(f'La palabra: {palabra1} tiene {diferencia} letra(s) más que la segunda palabra: {palabra2}')
elif cantidad2 > cantidad1:
    diferencia = cantidad2 - cantidad1
    print(f'La palabra: {palabra2} tiene {diferencia} letra(s) más que la primera palabra: {palabra1}')