#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario

nota1 = float(input("Digite la primera nota: "))
nota2 = float(input("Digite la segunda nota: "))
nota3 = float(input("Digite la tercera nota: "))
nota4 = float(input("Digite la cuarta nota: "))

promedio = (nota1+nota2+nota3+nota4)/4
print(f'El promedio de las notas ingresadas es: {promedio}')