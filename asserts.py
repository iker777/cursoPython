def primera_letra(lista_palabras):
    """ Trackea una palabra por cada for de lista_palabras
        1. El primer assert dice: 'si el elemento de palabra NO es 
            de tipo string, devuelve {palabra}no es string.
        
        2. El segundo assert dice, si la palabra no tiene carácteres, 
            devuelve 'no se permiten vacios' """
    primeras_letras = []
    
    for palabra in lista_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es String'
            assert len(palabra) > 0 , 'No se permiten vacios'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)

    return primeras_letras


lista = ['Angelo',5.5, '', 2 , '43952353', 0.35]
print('Primeras letras validas son : ' , primera_letra(lista))