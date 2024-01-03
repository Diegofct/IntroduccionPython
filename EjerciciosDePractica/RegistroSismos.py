listaCiudades = []
cantidadCiudades = 5 

for i in range(cantidadCiudades):
    ciudad = input("Escriba el nombre de la ciudad que desea registrar: ")
    listaCiudades.append(ciudad)

cantidadSismos = int(input("Ingrese la cantidad de sismos a registrar para cada ciudad: "))

registroSismos = []
for ciudad in listaCiudades:
    sismosCiudad = []
    print(f"Registro de sismos para {ciudad}:")
    
    for j in range(cantidadSismos):
        sismo = float(input(f"Ingrese la magnitud del sismo {j + 1}: "))
        sismosCiudad.append(sismo)

    registroSismos.append((ciudad, sismosCiudad))

print("\nRegistro de sismos:")
for ciudad, sismosCiudad in registroSismos:
    print(f"{ciudad}: {sismosCiudad}")

print(f"\nInforme de riesgos por ciudad:")
for ciudad, sismosCiudad in registroSismos:
    promedioSismos = sum(sismosCiudad)/len(sismosCiudad)
    print(f"El promedio de sismos para {ciudad} es: {promedioSismos}")

    if promedioSismos < 2.5:
        print(f"Para {ciudad} con promedio de {promedioSismos} es riesgo Amarillo(sin riesgo)")
    elif 2.6 <= promedioSismos <= 4.5:
        print(f"Para {ciudad} con promedio de {promedioSismos} es riesgo Naranja(riego medio)")
    else:
        print(f"Para {ciudad} con promedio de {promedioSismos} es riesgo Rojo(alto riego de terremoto)")
