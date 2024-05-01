while True:

    contadorPrimario = 0

    k = 0

    while True:

        respostas = ["sistemaoperacional", "abstração", "software", "hardware", "macos", "ios", "android", "windows", "sistemaComputação"]

        dicas = ["Software responsável por controlar hardware e os programas do sistema",
               "Conceito que destcar a importância de simplificar algo complexo",
               "Toda função digital de um computador ou também a parte interna",
               "Todo componente eletrônico ou mecânico de um computador",
               "Sistema Operacional para computador da Apple",
               "Sistema Operacional para celular da Apple",
               "Sistema Operacional para celular da Google",
               "Sistema Operacional para computador da Microsoft",
               "Junção de Hardware, Software e Sistema Operacional em um único dispositivo"]

        z = 0

        recebeEspacosForca = []

        x = 0

        certo = 0

        errar = 0

        b = 0

        errado = 3

        letra = 0

        branco = 0

        tudo = len(respostas[contadorPrimario])

        print(dicas[contadorPrimario])

        while True:

            print()

            while z != tudo:

                if respostas[contadorPrimario][k] == " ":

                    recebeEspacosForca.append(" ")

                    branco += 1

                else:

                    recebeEspacosForca.append("_")

                z += 1

            p = " ".join(recebeEspacosForca)

            print("Forca: %s" % p)

            print()

            letra = input("Digite uma letra: ").lower()

            print()

            if letra == "" or letra == " ":

                print("Não é permitido espaço em branco")

                continue

            elif letra in p:

                print("Esta letra já foi digitada!")

                continue

            if letra.isalpha():

                if len(letra) == 1:

                    while x != tudo:

                        if letra == respostas[contadorPrimario][x]:

                            recebeEspacosForca[x] = letra

                            certo += 1

                        else:

                            errar += 1

                        if errar == len(recebeEspacosForca):

                            errado -= 1

                            print("Letra errada!!!")

                        x += 1

                else:

                    print("Digite somente uma letra. Não é permitido mais de uma letra por vez na forca")

                    continue

                x = 0

                errar = 0

            else:

                print("Digite somente letras!")

                continue

            if errado == 0 or (certo + branco) == len(recebeEspacosForca):

                break

        if errado == 0:

            print("Você esgotou suas chances de errar. Enforcado!")

            print()

            print("   O ")

            print("   /\ ")

            print("   || ")

            print("-\   /-")

            print()

            while b != 5:

                print("  \O/" * 5)

                print("  \O/" * 5)

                b += 1

                print()

            break

        if (certo + branco) == len(recebeEspacosForca):

            print("Você acertou a palavra %s e não foi enforcado!" % respostas[contadorPrimario])

            contadorPrimario += 1

            if contadorPrimario == len(dicas):

                contadorPrimario = 0

            print()