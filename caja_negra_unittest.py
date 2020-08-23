import unittest
    # Unit test es una librería que sirve para testear código
    # Unit test: tipo de test que analiza cada función INDEPENDIENTEMENTE
    #Integration test: Tipo de test que analiza que las funciones vayan bien entre ellas

def suma(num_1, num_2):
    """ Suma dos números, siendo el primero de ellos Valor Absoluto """
    return abs(num_1) + num_2


class CajaNegraTest(unittest.TestCase):
    """ 1. Creamos una clase
        2. Metemos todo nuestro código de prueba dentro de la clase """

    def test_suma_dos_positivos(self):
        """ Self se utiliza en los objetos para llamar
            a un método """
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        #Prueba: Si resultado = 15. No hay fallos en mi código
        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        #assertEqual es uno de los métodos de la librería unittest
        self.assertEqual(resultado, 3)

#Buena práctica: Corremos el método unittest.main(), unittest.main() es la función principal
#Que corre dentro de la librería unittest
if __name__ == '__main__':
    unittest.main()