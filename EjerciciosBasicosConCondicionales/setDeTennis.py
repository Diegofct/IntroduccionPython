'''
Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, pero además debe haber ganado por lo menos dos juegos más que su rival. Si el set está empatado a 5 juegos, el ganador es el primero que llegue a 7. Si el set está empatado a 6 juegos, el set se define en un último juego, en cuyo caso el resultado final es 7-6.
'''

juegos_A = int(input("Número de juegos ganados por el jugador A: "))
juegos_B = int(input("Número de juegos ganados por el jugador B: "))

if not (0 <= juegos_A <= 7 and 0 <= juegos_B <= 7):
    print("Resultado inválido")
else:
    if (juegos_A == juegos_B) == 6:
        print("Set no terminado, se define a un punto")
    elif juegos_A == 7 and juegos_B < 5:
        print("A ganó el set")
    elif juegos_B == 7 and juegos_A < 5:
        print("B ganó el set")
    elif juegos_A == 7 and 5 <= juegos_B <= 6:
        print("A ganó el set")
    elif juegos_B == 7 and 5 <= juegos_A <= 6:
        print("B ganó el set")
    elif juegos_A == juegos_B == 5:
        print("Set no terminado, se define a dos puntos")
    else:
        print("Set no terminado")

