contadorPesoNormal = 0
contadorSobrepeso = 0
contadorObesidad1 = 0
contadorObesidad2 = 0
contadorObesidad3 = 0

for i in range(1, 21):
    nombreEstudiante = input(f"Escriba el nombre del estudiante {i}: ")
    edad = int(input(f"Escriba la edad del estudiante {i}: "))
    peso = float(input(f"¿Cuál es el peso del estudiante {i} en kg?: "))
    estatura = float(input(f"Escriba la estatura del estudiante {i}: "))

    imc = round(peso / estatura**2, 2)
    print(f"El imc del estudiante {i} es: {imc}")

    if imc >= 18.50 and imc <= 24.99:
        print(f"El estudiante {nombreEstudiante} de {edad} años, tiene un IMC normal. ")
        contadorPesoNormal += 1
    elif imc >= 25 and imc <= 29.99:
        print(f"El estudiante {nombreEstudiante} de {edad} años, tiene un IMC de sobrepeso. ")
        contadorSobrepeso += 1
    elif imc >= 30 and imc <= 34.99:
        print(f"El estudiante {nombreEstudiante} de {edad} años, tiene un IMC de obesidad 1. ")
        contadorObesidad1 += 1
    elif imc >= 35 and imc <= 39.99:
        print(f"El estudiante {nombreEstudiante} de {edad} años, tiene un IMC de obesidad 2. ")
        contadorObesidad2 += 1
    else:
        print(f"El estudiante {nombreEstudiante} de {edad} años, tiene un IMC de obesidad 3. ")
        # contadorObesidad3 += 1
        contadorObesidad3 = contadorObesidad3 + 1

print(f"{contadorPesoNormal} tienen un IMC Normal")
print(f"{contadorSobrepeso} tienen un IMC de Sobrepeso")
print(f"{contadorObesidad1} tienen un IMC de Obesidad grado 1")
print(f"{contadorObesidad2} tienen un IMC de Obesidad grado 2")
print(f"{contadorObesidad3} tienen un IMC de Obesidad grado 3")

