class Animal:
    # -La clase Animal crea animales.   
    # -PARÁMETROS ESPERADOS son:
    # tamano:'GRANDE', 'MEDIANO', 'PEQUEÑO'. str 
    # horas_dormidas_x_dia: 1 - 24 int
    #Se va a definir un parámetro privado llamado __energia

    def __init__(self, tamano, horas_dormidos_x_dia):
        self.tamano = tamano
        self.horas_dormidas_x_dia = horas_dormidos_x_dia

        if tamano == 'GRANDE':
            self.__energia = 50
        elif tamano == 'MEDIANO':
            self.__energia = 30
        elif tamano == 'MEDIANO':
            self.__energia = 20
        else:
            raise ValueError(f'El tamaño {tamano} no es un str válido. Las opciones son: GRANDE, MEDIANO, PEQUEÑO ')

    def energia_animal(self):
        print(self.__energia)


rinoceronte = Animal('GRANDE', 4)
rinoceronte.energia_animal()
