
def divide_elementos_de_lista(lista, divisor):
    """ Try es una pareja en la cual te cubres las espaldas ante una posible
        excepción."""
    
    #Si cuando hacemos "lo de dentro de try" sale el "except" ZeroDivisionError, haz "return lista". Te evitas un error
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(10))
divisor = int(input("Mete el divisor:   "))

print(divide_elementos_de_lista(lista, divisor))