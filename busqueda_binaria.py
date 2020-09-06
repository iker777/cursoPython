import random

def busqueda_binaria(lista, objetivo):
    lista.sort()
    comienzo = 0
    final = len(lista) - 1
    counter = 0

    while comienzo + 1 < final:
        counter += 1

        media = (comienzo + final) // 2

        if lista[media] == objetivo:
            return True, counter
        elif lista[media] > objetivo:
            final = media
        elif lista[media] < objetivo:
            comienzo = media
    
    return False, counter


if __name__ == '__main__':
    tamano_lista = int(input('De que tamano quieres la lista? \n: '))  # O(1)
    objetivo_int = int(input('qué número quieres encontrar?\n: '))  # O(1)

    lista_random = [random.randint(0, 100) for i in range(tamano_lista)] # O(x) # Genera números aleatorios del 0 al 100 en una lista del tamaño tamano_lista

    encontrado, contador = busqueda_binaria(lista_random, objetivo_int)  # Función Búsqueda_lineal = 2x + 3
    print(lista_random)  # O(1)
    print(f'El elemento {objetivo_int} {"esta" if encontrado else "no esta"} en la lista. {"resuelto en" if encontrado else "Veces iterado"} {contador} ')  # O(x)
