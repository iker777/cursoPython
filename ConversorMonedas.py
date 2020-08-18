def conversor(tipode_moneda, cambio_dolares):
    valor = str(input("Ingresa un valor en dolares:   "))
    valor_pesos = float(cambio_dolares) * float(valor)
    valor_pesos = str(round(valor_pesos, 2))
    print("el valor de "+ valor + "$ americanos" + " en "+ tipode_moneda +" es "+ valor_pesos +" $")


def run():
    menu = """
    Bienvenido al conversor de monedas

    1- Pesos colombianos
    2- Pesos argentinos
    3- Pesos mexicanos 

    Elige una opción
    """
    opcion = int(input(menu))

    if opcion == 1:
        conversor("pesos colombianos", 3681.20)

    elif opcion == 2:
        conversor("pesos argentino", 3681.20)

    elif opcion == 3:
        conversor("pesos mexicano", 3681.20)

    else:
        print("Opción no válida, por favor escoje entre una opción entre (1-2-3)")

if __name__ == '__main__':
    run()