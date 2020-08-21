def equation():
    print("Esta va a ser tu ecuación de tercer grado: Ax^3 + Bx^2 + Cx^3 = D. Introduce los factores de tu ecuación")
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    d = int(input("D: "))

    return a, b, c, d


def exhaustive_enumeration(var1, var2, var3, var4):
    pass

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
            exhaustive_enumeration(a,b,c,d)
            break

        elif option == 2:
            a,b,c,d = equation()
            approximation(a,b,c,d)
            break
        
        elif option == 3:
            a,b,c,d = equation()
            binary_search(a,b,c,d)
            break
    
    


if __name__ == '__main__':
    run()