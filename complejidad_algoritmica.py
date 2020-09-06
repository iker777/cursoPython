import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n -1)


if __name__ == '__main__':
    comienzo = time.time()
    print(factorial(10))
    final = time.time()
    print(final - comienzo)
    
    comienzo = time.time()
    print(factorial_r(10))
    final = time.time()
    print(final - comienzo)
    