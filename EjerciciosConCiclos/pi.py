def estimarPI(n):
    suma=0
    signo=1

    for i in range(n):
        termino = 1/(2*i+1)
        suma=suma+signo*termino
        signo*=-1
    
    estimacionPi = 4*suma
    return estimacionPi

n = int(input("Ingrese el número del termino para estimar pi: "))
print(estimarPI(n))