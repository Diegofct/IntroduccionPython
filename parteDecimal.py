#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

numeroReal = float(input("Digite un número con decimal: "))
parteEntera = int(numeroReal)
parteDecimal = round(numeroReal-parteEntera,2)

print(f'La parte decimal es: {parteDecimal}')