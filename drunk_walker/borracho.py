import random

class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre

class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0, 7), (0, -4), (10, 0), (-13, 0)])