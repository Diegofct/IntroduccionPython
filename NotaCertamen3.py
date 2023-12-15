C1 = float(input("Ingrese la nota del primer certamen: "))
C2 = float(input("Ingrese la nota del segundo certamen: "))
NL = float(input("Ingrese la nota del laboratorio: "))

NC = (C1 + C2) / 2

NF_objetivo = 60
C3_necesario = (NF_objetivo - 0.7 * NC) / 0.3

print(f"Para aprobar el ramo con una nota final de {NF_objetivo}, necesitas obtener al menos {C3_necesario:.2f} en el tercer certamen.")
