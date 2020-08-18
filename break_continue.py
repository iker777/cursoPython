def run():
    frase = str(input("Escribe la frase que quieras, te diré cuantas o-s hay \n"))
    frase = frase.lower().replace(" ", "")
    contador_deOs = 0
    for i in frase:
        if i == "o":
            contador_deOs = contador_deOs +1
        else:
            if i == "p":
                break
                
    print(contador_deOs)




if __name__ == '__main__':
    run()