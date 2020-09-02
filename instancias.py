class Coordenada:

    # Defines los atributos del objeto
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Defines el método
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        # Devuelve el módulo de diferencia entre las coordenadas
        return (x_diff + y_diff)**0.5


# Si este archivo se ejecuta desde la terminal, la podemos correr    
if __name__ == '__main__':
    # Llamas y defines los objetos
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)


    # coord_2 es una instancia de Coordenada? True or False?
    print(isinstance(coord_2, Coordenada))

    # Así se declara el método .distancia de la clase Coordenada
    print(coord_1.distancia(coord_2))