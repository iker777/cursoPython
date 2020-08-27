#import unittest
#import math

def finding_solution(var_A, var_B, var_C, var_D, limite_min, limite_max):
    a = limite_min
    b = limite_max
    fa = var_A*a**2 + var_B*a + var_C + var_D
    
    for i in range(100):
        fb = var_A*b**2 + var_B*b + var_C + var_D
        bolzano = fa * fb

        if fb < 0.001 and fb > -0.001:
            return round(b, 3)

        elif bolzano < 0:
            #Hay una raíz entre a y b
            limite_max = b
            #print('b más PEQUEÑA', b_max, b_min, b)
            b = (limite_max + limite_min)/2
            continue

        elif bolzano > 0:
            #No hay una raíz entre a y b
            limite_min = b
            #print('b más GRANDE', b_max, b_min, b)
            b = (limite_max + limite_min)/2
            continue
        
    return "No tiene respuesta"

def bolzano(A, B, C, D):
    print("Esta va a ser tu ecuación de tercer grado: Ax^2 + Bx + C + D = 0. Introduce los factores de tu ecuación")
    # A = float(input("A: "))
    # B = float(input("B: "))
    # C = float(input("C: "))
    # D = float(input("D: "))
    # A = float(1)
    # B = float(0)
    # C = float(-5)
    # D = float(0)

    sol1_min = float(0.1)
    sol1_max = float(1000)
    sol1 = finding_solution(A, B, C, D, sol1_min, sol1_max)

    sol2_min = float(-1000)
    sol2_max = sol1 - 0.5
    sol2 = finding_solution(A, B, C, D, sol2_min, sol2_max)

    return sol1, sol2
    

if __name__ == '__main__':
    bolzano(A, B, C, D)