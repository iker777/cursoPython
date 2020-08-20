import random


# def es_correcto():


#     if numero_usuario == numero_random:
#         print("Felicidades TXO! Has acertado :)")
#         return True

#     elif numero_usuario > numero_random:
#         numero_usuario = int(input("Tu número es más grande, vuelve a intentarlo:   "))
#         print(numero_usuario)
#         return False

#     elif numero_usuario < numero_random:
#         numero_usuario = int(input("Tu número es más pequeño, vuelve a intentarlo:   "))
#         print(numero_usuario)
#         return False


def run():    
    numero_random = random.randint(1, 100)
    numero_usuario = int(input("Di un número del 1 al 100, a que no adivinas:   "))
    print(numero_usuario, numero_random)

    while numero_usuario != numero_random:
        if numero_usuario > numero_random:
            numero_usuario = int(input("Tu número es más grande, vuelve a intentarlo:   "))

        elif numero_usuario < numero_random:
            numero_usuario = int(input("Tu número es más pequeño, vuelve a intentarlo:   "))
    print("Has acertado TXO!")

            
if __name__ == '__main__':
    run()