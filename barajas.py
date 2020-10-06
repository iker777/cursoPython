import random

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey', 'as']
ESCALA_DE_VALOR = ['CARTA ALTA', 'PAREJA', 'DOBLE PAREJA', 'TRIO', 'ESCALERA', 'DOBLE PAREJA', 'COLOR', 'FULL', 'POKER', 'ESCALERA DE COLOR', 'ESCALERA REAL']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano=5):
    mano = random.sample(barajas, tamano_mano)
    
    return mano

def quien_gana(mano_j1, mano_j2):
    manos_en_lista = [mano_j1, mano_j2]
    iterar_palos = len(PALOS) - 1
    dict_jugadores = {}
    
    for mano_valor in range(manos_en_lista):
        for i in iterar_palos:
            palos = []
            palos += 5 * [PALOS[i]]
            palos_dela_mano = list(mano_valor.keys())

            if palos == palos_dela_mano:
                if  
                    jugador = 'ESCALERA REAL'
                elif
                    jugador = 'ESCALERA DE COLOR'
                else:
                    jugador = 'COLOR'
             
        
        if 4 cartas iguales FULL

        if 3 cartas iguales FULL o TRIO

        if 2 cartas iguales DOBLE PAREJA O PAREJA

        else:
            jugador = 'CARTA ALTA'

        ¿Cuál es la carta más alta del jugador?  

        dict_jugadores.update({jugador:carta_alta})






    if ganador == jugador1:
        print(f'el ganador ha sido el jugador 1 con la mano:\n {mano_j1}')
        return 'Jugador1'
    else:
        print(f'el ganador ha sido el jugador 2 con la mano:\n {mano_j2}')
        return 'Jugador2'



def main(intentos, tamano_mano=5):
    barajas = crear_baraja()
    marcador = [0, 0]

    manos = []
    for i in range(intentos):
        mano_j1 = obtener_mano(barajas, tamano_mano)
        mano_j2 = obtener_mano(barajas, tamano_mano)
        print(f'la mano número {i + 1} del jugador 1 es: {mano_j1}')
        print(f'la mano número {i + 1} del jugador 2 es: {mano_j2}')

        ganador = quien_gana(mano_j1, mano_j2)
        print(f'El ganador ha sido el {ganador}')

        if ganador == 'Jugador1':
            marcador[0] += 1
        elif ganador == 'Jugador2':
            marcador[1] += 1

    if marcador[0] == marcador[1]:
        print(f"En {intentos} intentos no ha ganador nadie EMPATE")
    else:
        print(f"el ganador en {intentos} intentos ha sido el {'jugador 1' if marcador[0] > marcador[1] else 'jugador 2'}")
    


if __name__ == '__main__':
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))
    main(intentos)