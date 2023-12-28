#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas.

horaActual = float(input("Digite la hora actual: "))
cantidadHoras = int(input("Ingrese un número cualquiera para saber qué hora marcará: "))

sumarHoras = horaActual+cantidadHoras

if sumarHoras < 24:
    print(f'En {cantidadHoras} horas, serán las {sumarHoras}')
else:
    hora = (sumarHoras%24)
    print(f'En {cantidadHoras} horas, serán las {hora}')
    
