class Animal:
    # -La clase Animal crea animales.   
    # -PARÁMETROS ESPERADOS son:
    # tamano:'GRANDE', 'MEDIANO', 'PEQUEÑO'. str 
    # horas_dormidas_x_dia: 1 - 24 int
    #Se va a definir un parámetro privado llamado __energia

    def __init__(self, tamano, horas_dormidos_x_dia):
        self.tamano = tamano
        self.horas_dormidas_x_dia = horas_dormidos_x_dia
        self.__counter = 0

        if tamano == 'GRANDE':
            self.energia = 50
        elif tamano == 'MEDIANO':
            self.energia = 30
        elif tamano == 'PEQUEÑO':
            self.energia = 20
        else:
            raise ValueError(f'El tamaño {self.tamano} no es un str válido. Las opciones son: GRANDE, MEDIANO y PEQUEÑO ')

    def dia(self, comer):
        """ 
            El método dia simula el paso de un día donde el animal come (Mucho) o (Poco). 
            Si el animal come 5 o más, tiene + 10 de energía
            Si el animal come menos de 5, tiene + 5 de energía

            Llamas al método con el argumento comer, un integer

        """
        self.__counter += 1
        self.comer = comer
        if comer < 5:
            self.energia += 5
        else:
            self.energia += 10

        print(f'Hoy es dia {self.__counter} para nuestro Animal y tiene {self.energia} de energia')

    @property
    def energiaAnimal(self):
        """
            Te informa del día en el que estamos y la energía del animal.
        """
        print(f'Su energía el día {self.__counter} es de {self.energia}')

    @energiaAnimal.setter
    def energiaAnimal(self, nueva_energia):  # El atributo name es el atributo que estamos tratando de insertar como atributo
        self.energia = nueva_energia
        return self.energia



class Gusano(Animal):
    def __init__(self):
        Animal.__init__(self, "PEQUEÑO", 2)
        self.__agujero = 0

    def agujero(self):
        self.energia -= 20
        if self.energia < 0:
            print(f'RIP Gusanito por hacer tantos agujeritos, murió con {self.__agujero} agujeritos')
        else:
            self.__agujero += 1
            print(f'Gusanito sigue VIVITO y con {self.__agujero} agujeros')


if __name__ == '__main__':
    gusanito = Gusano()
    gusanito.agujero()
    while gusanito.energia < 21:
        gusanito.dia(6)

    gusanito.agujero()
    gusanito.energiaAnimal




