def factorial(n):
    """Calcula el factorial de n. """
    
    if n == 1:
        print()
        return 1
    
    print(n)
    return n * factorial(n - 1)


def run():
    user_n = int(input("Mete el número que quieras factorizar:  "))
    print(factorial(user_n))

if __name__ == '__main__':
    run()