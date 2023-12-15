#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento

from datetime import date

diaNacimiento = int(input("Ingrese el número del día de su nacimiento: "))
mesNacimiento = int(input("Digite el número del mes de su nacimiento: "))
añoNacimiento = int(input("Digite el año de su nacimiento: "))

fechaHoy = date.today()
añoActual = fechaHoy.year
mesActual = fechaHoy.month
diaActual = fechaHoy.day

# edad = añoActual - añoNacimiento
# print(f'Usted tiene {edad} años')

# if mesNacimiento<mesActual:
#     print(f'Usted ya cumplió años')
# elif diaNacimiento>diaActual and mesNacimiento>=mesActual :
#     edad-=1
#     print(f'Usted está por cumplir años')
# elif diaNacimiento==diaActual and mesNacimiento==mesActual :
#     print(f'Hoy es su cumpleaños, felicidades')

# edadPendiente = (añoActual-añoNacimiento)-1
# while diaNacimiento>diaActual and mesNacimiento>=mesActual:

#     if mesNacimiento<mesActual:
#         edadActual = (añoActual-añoNacimiento)
#         print(f'Usted ya cumplió años y tiene {edadActual} años')
#     elif diaNacimiento>diaActual and mesNacimiento>=mesActual :
#         print(f'Usted tiene {edadPendiente} y está por cumplir años')
#     elif diaNacimiento==diaActual and mesNacimiento==mesActual :
#         print(f'Hoy cumples {edadActual} años, felicidades')
