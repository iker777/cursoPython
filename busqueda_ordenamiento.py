import random

def bubbleSort(lista):  # O(n) * O(n - i - 1) = n**2  Crecimiento exponencial. Es un mal algoritmo
    
    counter = 0
    n = len(lista)

    for j in range(n - 1):

        for i in range(n - j - 1):
            counter += 1

            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

    return lista, counter


def ordenamiento_por_insercción(lista):
    counter = 0

    for indice in range(1, len(lista)):
        print(lista)
        counter += 1
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista, counter

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        # llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista



if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)



# if __name__ == '__main__':
#     n = int(input("Elige el tamaño de tu lista:  "))
#     lista_desordenada = [random.randint(0, 100) for i in range(n)]
#     print(lista_desordenada)
#     lista_ordenada, contador = ordenamiento_por_insercción(lista_desordenada)
#     print(lista_ordenada,"\n",f'Han hecho falta {contador} veces para ordenar la lista')

