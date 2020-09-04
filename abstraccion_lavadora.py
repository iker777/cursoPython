
class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):  # Temperatura es un atributo predeterminado que el usuario no tiene que definir
        self.__llenar_tanque_de_agua(temperatura)  # Los atributos o métodos internos (que no hace falta llamar desde fuera, se definen con una _delante)
        self.__anadir_jabon()
        self.__lavar()
        self.__centrifugar()

    def __llenar_tanque_de_agua(self, temperatura):  # Los métodos privados también se definen con una _delante
        print('Llenando el tanque con agua ', str(temperatura) )

    def __anadir_jabon(self):
        print('Anadiendo jabon')

    def __lavar(self):
        print('Lavando la ropa')

    def __centrifugar(self):
        print('Centrifugando la ropa')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
    lavadora.__centrifugar()  # Esta no va a funcionar porque es un atributo privado
