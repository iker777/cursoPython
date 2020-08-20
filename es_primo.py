def es_primo(numero):
    for i in range(numero+1, 1):
        resto = numero % i
        if resto == 0:
            return True
        if i == numero:
            return False

        
def run():
    numero = 0
    while numero == 0:
        numero = int(input("Escribe tu número aquí si quieres saber si es primo o no (no vale 0) \n"))
        numero = round(numero)
        numero_print = str(numero)
    if numero < 0:
        numero = -numero
    if es_primo(numero) == True:
        print(numero_print + " No es Primo")
    else:
        print(numero_print + " No es Primo")


if __name__ == '__main__':
    run()
range