import random

# Analizar la complejidad algorítmica del programa

def busqueda_lineal(lista, objetivo):
    match = False  # O(1)

    for elemento in lista:  # Complejidad algoritmica. O(x)
        if elemento == objetivo:  # O(1)
            match = True  # O(1)
            break  # O(1)

    return match  # O(1)


if __name__ == '__main__':
    tamano_lista = int(input('De que tamano quieres la lista?'))  # O(1)
    objetivo = int(input('qué número quieres encontrar?'))  # O(1)

    lista = [random.randint(0, 100) for i in range(tamano_lista)] # O(x) # Genera números aleatorios del 0 al 100 en una lista del tamaño tamano_lista

    encontrado = busqueda_lineal(lista, objetivo)  # Función Búsqueda_lineal = 2x + 3
    print(lista)  # O(1)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')  # O(x)

    # Complejidad algorítmica: 0(x) lineal