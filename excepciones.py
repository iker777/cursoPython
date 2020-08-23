
def divide_elementos_de_lista(lista, divisor):
    """ Try es una pareja en la cual te cubres las espaldas ante una posible
        excepción."""
    
    #Si cuando hacemos "esto" sale el "except" ZeroDivisionError, haz "esto"
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(10))
divisor = int(input("Mete el divisor:   "))

print(divide_elementos_de_lista(lista, divisor))