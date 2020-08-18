def palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    palabra_inversa = palabra[::-1]
    
    if palabra == palabra_inversa:
        return True
    else:
        return False


def run():
    menu = "1"
    while menu == "1":

        palabra = str(input("Escribe una o varias palabras y te diremos si es Palíndromo \n"))
        es_palindromo = palindromo(palabra)

        if es_palindromo == True:
            print("La palabra " + palabra + " Es palíndromo")
        else:
            print("La palabra " + palabra + " No es palíndromo")

        menu = str(input("Si quieres volver a proponer una palabra, escribe 1. Si no, cualquier otra tecla \n"))


if __name__ == '__main__':
    run()