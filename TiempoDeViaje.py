
# Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.
# Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
# El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

total_minutos = 0

while True:
    tiempo_tramo = int(input("Ingrese la duración del tramo en minutos (ingrese 0 para finalizar): "))
    
    if tiempo_tramo == 0:
        break

    total_minutos += tiempo_tramo

horas = total_minutos // 60
minutos = total_minutos % 60

print(f"Tiempo total de viaje: {horas} horas y {minutos} minutos")
