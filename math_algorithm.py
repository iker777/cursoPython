def equation():
    print("Esta va a ser tu ecuación de tercer grado: Ax^3 + Bx^2 + Cx^3 = D. Introduce los factores de tu ecuación")
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    d = int(input("D: "))

    return a, b, c, d


def exhaustive_enumeration(var1, var2, var3, var4):
    x = 0
    solution = var1 * x**2 + var2 * x + var3
    cycle = True

    while cycle == True:
        if solution == var4:
            break
            return x
        
        elif solution > var4:
            x = x - 1

        elif solution < var4:
            x = x + 1


    

def approximation(var1, var2, var3, var4):
    pass


def binary_search(var1, var2, var3, var4):
    pass


def run():
    cycle = True

    while cycle == True:
        option = int(input("""   ELIGE CON QUÉ MÉTODO QUIERES RESOLVER LA ECUACIÓN:
                                    
                                    1. Enumeración exhaustiva
                                    2. Aproximación
                                    3. Búsqueda binaria   
                                    
                                    Elige:  """))

        if option == 1:
            a,b,c,d = equation()
            answer = exhaustive_enumeration(a,b,c,d)
            print(answer)
            break

        elif option == 2:
            a,b,c,d = equation()
            answer = approximation(a,b,c,d)
            print(answer)
            break
        
        elif option == 3:
            a,b,c,d = equation()
            answer = binary_search(a,b,c,d)
            print(answer)
            break
    
    


if __name__ == '__main__':
    run()