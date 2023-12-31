def todos_iguales(lista):
    for i in range(1, len(lista)):
        if lista[i] != lista[i - 1]:
            print(f"Los números no son todos iguales.")
            return False

    print(f"Todos los números son iguales.")
    return True

sonIguales = todos_iguales([6, 3, 2])
