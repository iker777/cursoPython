class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None
 
    @property  # Definir el siguiente método como property
    def region(self):  # El método region tiene que cumplir lo de abajo:
        return self.__region
 
    @region.setter  #Con este decorador @metodo.setter --> Le pones unas condiciones a los valores de entrada 
    def region(self, region):
        if region in self.__pais:  # Si la región está dentro de la lista, devuelve la región. Está bien.
            self.__region = region
        else:
            raise ValueError(f'La region {region} no esta en la lista')  # Si  no ERROR
 
 
casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
print(casilla.region)
casilla.region = 'Mexic'
print(casilla.region)