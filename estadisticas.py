import random
import math

def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2

    return acumulador / len(X)


def desviacion_estandar(X):
    return math.sqrt(varianza(X))

if __name__ == '__main__':
    X = [random.randint(1, 21) for _ in range(10)]
    print(X)
    print(f'la media de la lista es: {media(X)}')
    print(f'la varianza de la lista es: {varianza(X)}')
    print(f'la desviación estandar de la lista es: {desviacion_estandar(X)}')