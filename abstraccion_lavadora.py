
class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):  # Temperatura es un atributo predeterminado que el usuario no tiene que definir
        self._llenar_tanque_de_agua(temperatura)  # Los atributos o métodos internos (que no hace falta llamar desde fuera, se definen con una _delante)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar

    def _llenar_tanque_de_agua(self, temperatura):  # Los métodos privados también se definen con una _delante
        print('Llenando el tanque con agua ', str(temperatura) )

    def _anadir_jabon(self):
        print('Anadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
