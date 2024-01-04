import json

campers = []

def registrar_camper():
    nombre = input("Escriba el nombre del estudiante: ")
    apellidos = input("Escriba los apellido del estudiante: ")
    identificacion = int(input("Digite el número de cédula o identificación del estudiante: "))
    direccion = input("Escriba la dirección de residencia: ")
    acudiente = input("Escriba el nombre de un acudiente: ")
    celular = int(input("Digite el número de celular: "))
    fijo = int(input("Digite el número de teléfono fijo: "))

    camper = {
        "nombre": nombre,
        "apellidos": apellidos,
        "NroIdentificación": identificacion,
        "Dirección": direccion,
        "Acudiente": acudiente,
        "NroCelular": celular,
        "TeléfonoFijo": fijo
    }

    campers.append(camper)
    
    print(f"Camper registrado exitosamente")


def visualizar_campers():
    print("\nLista de Campers:")
    for i, camper in enumerate(campers, start=1):
        print(f"\nCamper {i}:")
        for key, value in camper.items():
            print(f"{key}: {value}")
    
    estudiantes = json.dumps(campers)
    file = open("estudiantes.json","w")
    file.write(estudiantes)
    file.close()

while True:
    print("\nMenú:")
    print("1. Registrar Camper")
    print("2. Visualizar Campers")
    print("3. Salir")

    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        registrar_camper()
    elif opcion == "2":
        visualizar_campers()
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")