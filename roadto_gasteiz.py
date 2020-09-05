class Car:
    # Definir los atributos del objeto
    def __init__(self, brand, weight, max_speed):
        self.brand = brand  # Atributos públicos
        self.weight = weight
        self.max_speed = max_speed

    def time_to_arrive(self, road_distance):  # Método de Car
        return road_distance / self.max_speed


class Road:  # Creamos la clase Road
    def __init__(self, distance):  # Solo definimos un atributo público
        self.distance = distance


if __name__ == '__main__':  # Así ejecutamos el código 'Buena práctica'. "si el programa se llama desde la terminal, ejecuta"
    forfi = Car("Ford", 1000, 120)  # Llamamos al Objeto Car y la metemos en la variable forfi
    road_gasteiz = Road(100)  # La clase Road() será la variable road_gasteiz
    print(forfi.time_to_arrive(road_gasteiz.distance))  #Imprime el método time_to_arrive de la variable forfi. Donde la variable sea la distancia del objeto de road_gasteiz