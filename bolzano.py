import unittest
import math


def bolzano():
    print("Esta va a ser tu ecuación de tercer grado: Ax^2 + Bx + C + D = 0. Introduce los factores de tu ecuación")
    A = float(input("A: "))
    B = float(input("B: "))
    C = float(input("C: "))
    D = float(input("D: "))
    # A = float(1)
    # B = float(0)
    # C = float(-5)
    # D = float(0)

    a = float(0.1)
    fa = A*a**2 + B*a + C + D
    b = float(100)
    b_max = b
    b_min = a

    for i in range(100):
        fb = A*b**2 + B*b + C + D
        bolzano = fa * fb

        if fb < 0.001 and fb > -0.001:
            return round(b, 4)

        elif bolzano < 0:
            #Hay una raíz entre a y b
            b_max = b
            #print('b más PEQUEÑA', b_max, b_min, b)
            b = (b_max + b_min)/2
            continue

        elif bolzano > 0:
            #No hay una raíz entre a y b
            b_min = b
            #print('b más GRANDE', b_max, b_min, b)
            b = (b_max + b_min)/2
            continue
        
    return "No tiene respuesta"
            
class TestBolzano(unittest.TestCase):
    def test_run(self):
        solution = bolzano()
        print("la respuesta de x es: " + str(solution))
        self.assertEqual(solution, round(math.sqrt(5), 4))

if __name__ == '__main__':
    unittest.main()