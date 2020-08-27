def equation():
    print("Esta va a ser tu ecuación de tercer grado: Ax^2 + Bx + C = D. Introduce los factores de tu ecuación")
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    d = int(input("D: "))

    return a, b, c, d


def exhaustive_enumeration(var1, var2, var3, var4):
    """El método exhaustivo​ es un procedimiento geométrico
     de aproximación a un resultado, con el cual el grado de 
     precisión aumenta en la medida en que avanza el cálculo."""

    for x in range(-500, 501):
        solution = var1 * x**2 + var2 * x + var3

        if solution == var4:
            return x
            break
        
        elif x == 500:
            print("No hemos encontrado respuesta con este método, vuelve a intentarlo")


def bolzano(var1, var2, var3, var4):
    var1 = float(var1)
    var2 = float(var2)
    var3 = float(var3)
    var4 = float(var4)
    fa = -var1
    b = 100
    b_old = []

    for i in range(100):
        fb = var1 * b**2 + var2 * b + var3 - var4
        is_negative = fa *fb
        b_old.append(b)

        if is_negative == True:
            b = ( b_old[i-2] - b ) / 2

        elif is_negative == False:
            b = ( b_old[i-2] - b ) / 2

        if solution == 0:
            return x

        elif i == 100:
            print("No hemos encontrado respuesta con este método, vuelve a intentarlo")



def binary_search(var1, var2, var3, var4):
    pass


def run():
    cycle = True

    while cycle == True:
        option = int(input("""   ELIGE CON QUÉ MÉTODO QUIERES RESOLVER LA ECUACIÓN:
                                    
                                    1. Enumeración exhaustiva
                                    2. Bolzano
                                    3. Búsqueda binaria   
                                    
                                    Elige:  """))

        if option == 1:
            a,b,c,d = equation()
            answer = exhaustive_enumeration(a,b,c,d)

            if answer != None:
                break

        elif option == 2:
            a,b,c,d = equation()
            answer = bolzano(a,b,c,d)
            if answer != None:
                break
        
        elif option == 3:
            a,b,c,d = equation()
            answer = binary_search(a,b,c,d)
            if answer != None:
                break

    print("La respuesta es: " + str(answer))
    
    


if __name__ == '__main__':
    run()