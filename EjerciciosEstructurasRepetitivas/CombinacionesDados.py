valorDado1 = int(input("Digite el valor que obtuvo con el dado1: "))
valorDado2 = int(input("Digite el valor que obtuvo con el dado2: "))
contarCombinaciones = 0

puntaje = valorDado1 + valorDado2

for dado1 in range(1,7):
    for dado2 in range(1,7):
        if dado1 + dado2 == puntaje:
            contarCombinaciones+=1

print(f"Para el puntaje {puntaje}, hay {contarCombinaciones} combinaciones posibles.")