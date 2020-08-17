def conversor(tipode_moneda, valor, opcion):
    valor = str(input("Ingresa un valor en dolares:   "))
    if opcion == 1:
        valor_dolar = float(3681.20)
    elif opcion == 2:
        valor_dolar = float(74.67)
    elif opcion == 3:
        valor_dolar = float(22.28)
    valor_pesos = valor_dolar * float(valor)
    valor_pesos = str(round(valor_pesos, 2))
    print("el valor de "+ valor + "$ americanos" + " en "+ tipode_moneda +" es "+ valor_pesos +" $")



menu = """
Bienvenido al conversor de monedas

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos 

Elige una opción
"""
opcion = int(input(menu))

if opcion == 1:
    conversor("pesos colombianos", valor, opcion)

elif opcion == 2:
    conversor("pesos argentino", valor, opcion)

elif opcion == 3:
    conversor("pesos mexicano", valor, opcion)

else:
    print("Opción no válida, por favor escoje entre una opción entre (1-2-3)")