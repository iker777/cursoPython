def fibonacci(n):
    """ Crea una seguida de Fibonacci hasta el elemento numero n
        de la seguida. ENSAYAR UNA FUNCIÓN RECURSIVA    """
    
    if n == 1 or n == 0:
        print(1)
        return 1
    
    print(n)
    return n + fibonacci(n - 1)


def run():
    user_n = int(input("Introduce el elemento en el que quieres que se acabe la seguida de fibonnacci:  "))

    if user_n < 0:
        user_n = -user_n

    print(fibonacci(user_n))


if __name__ == '__main__':
    run()
     