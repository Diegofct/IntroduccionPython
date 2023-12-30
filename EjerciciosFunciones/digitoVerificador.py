def obtener_rol():
    rol = int(input("Ingrese el número o rol: "))
    return rol

def invertir_numero(numero):
    numeroStr = str(numero)
    longitud = len(numeroStr)
    sliced_str = numeroStr[::-1]
    return sliced_str

def multiplicar_por_secuencia(numero):
    numero_str = str(numero)
    longitud = len(numero_str)
    secuencia = [2, 3, 4, 5, 6, 7]

    resultado = []

    for i in range(longitud):
        digito = int(numero_str[i])
        multiplicador = secuencia[i % len(secuencia)]
        resultado.append(digito * multiplicador)
        suma_numeros_multiplicados = sum(resultado)

    return suma_numeros_multiplicados

def obtener_digito_verificador(numero):

    numero_str = str(numero)
    longitud = len(numero_str)

    resultado_suma = multiplicar_por_secuencia(numeroInvertido)
    sacar_modulo = resultado_suma % 11
    digitoVerificador = 11 - sacar_modulo
    return digitoVerificador



numeroRol = obtener_rol()
numeroInvertido = invertir_numero(numeroRol)
print(f"Número invertido: {numeroInvertido}")

numeroMultiplicado = multiplicar_por_secuencia(numeroInvertido)
print(f"El resultado de la suma al multiplicar por la secuencia es: {numeroMultiplicado} ")

obtenerVerificador = obtener_digito_verificador(numeroInvertido)
print(f'El rol con su verificador sería el siguiente: {numeroRol}-{obtenerVerificador}')