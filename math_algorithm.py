import bolzano
import math

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


def equation_dbh(var1, var2, var3, var4):
    sol1 = round((-var2 + math.sqrt(var2**2 - 4*var1 * (var3 + var4))) / 2*var1, 3)
    sol2 = round((-var2 - math.sqrt(var2**2 - 4*var1 * (var3 + var4))) / 2*var1, 3)
    return sol1, sol2


def run():
    cycle = True

    while cycle == True:
        option = int(input("""   ELIGE CON QUÉ MÉTODO QUIERES RESOLVER LA ECUACIÓN:
                                    
                                    1. Enumeración exhaustiva
                                    2. Bolzano
                                    3. Ecuación típica de DBH   
                                    
                                    Elige:  """))

        if option == 1:
            a,b,c,d = equation()
            answer = exhaustive_enumeration(a,b,c,d)
            print("La respuesta es: " + str(answer))

            if answer != None:
                break

        elif option == 2:
            a, b, c, d = equation()
            solution1, solution2 = bolzano.bolzano(a, b, c, d)
            print("la respuesta de x son --> solución1: " + str(solution1) + "\n                      --> y solución2: " + str(solution2))

            if solution1 != str or solution2 != str:
                break
        
        elif option == 3:
            a,b,c,d = equation()
            solution1, solution2 = equation_dbh(a, b, c, d)
            print("la respuesta de x son --> solución1: " + str(solution1) + "\n                      --> y solución2: " + str(solution2))

            if solution1 != str or solution2 != str:
                break  


if __name__ == '__main__':
    run()