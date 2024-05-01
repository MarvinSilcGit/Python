print()

print("Essas são as posições correspondentes ao teclado numérico: ")

print()

print(" 7  |  8 |  9")

print("---+---+---")

print(" 4  |  5 |  6")

print("---+---+---")

print(" 1  |  2 |  3")

while True:

    x = 1

    d = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]

    while True:

        print()

        jog1 = input("Jogador %d, posição: " % x)

        if jog1.isdigit() == True:

            if len(jog1) == 1:

                print()

                jog2 = int(jog1)

                if jog2 >= 1:

                    if d[jog2-1] != "  ":

                        print("Local ocupado!")

                        continue

                    else:

                        if x == 1:

                            d[jog2-1] = "x"

                            x += 1

                        elif x == 2:

                            d[jog2-1] = "o"

                            x -= 1

                    print(" %s  |  %s |  %s" % (d[6], d[7], d[8]))

                    print("---+---+---")

                    print(" %s  |  %s |  %s" % (d[3], d[4], d[5]))

                    print("---+---+---")

                    print(" %s  |  %s |  %s" % (d[0], d[1], d[2]))

                    print()

                    if "x" in d[0] and "x" in d[1] and "x" in d[2] or "o" in d[0] and "o" in d[1] and "o" in d[2]:

                        print("Fim de jogo")

                        break

                    elif "x" in d[3] and "x" in d[4] and "x" in d[5] or "o" in d[3] and "o" in d[4] and "o" in d[5]:

                        print("Fim de jogo")

                        break

                    elif "x" in d[6] and "x" in d[7] and "x" in d[8] or "o" in d[6] and "o" in d[7] and "o" in d[8]:

                        print("Fim de jogo")

                        break

                    elif "x" in d[0] and "x" in d[3] and "x" in d[6] or "o" in d[0] and "o" in d[3] and "o" in d[6]:

                        print("Fim de jogo")

                        break

                    elif "x" in d[1] and "x" in d[4] and "x" in d[7] or "o" in d[1] and "o" in d[4] and "o" in d[7]:

                        print("Fim de jogo")

                        break

                    elif "x" in d[2] and "x" in d[5] and "x" in d[8] or "o" in d[2] and "o" in d[5] and "o" in d[8]:

                        print("Fim de jogo")

                        break

                    elif "x" in d[0] and "x" in d[4] and "x" in d[8] or "o" in d[0] and "o" in d[4] and "o" in d[8]:

                        print("Fim de jogo")

                        break

                    elif "x" in d[2] and "x" in d[4] and "x" in d[6] or "o" in d[2] and "o" in d[4] and "o" in d[6]:

                        print("Fim de jogo")

                        break

                    elif d[0] != "  " and d[1] != "  " and d[2] != "  " and d[3] != "  " and d[4] != "  " and d[5] != "  " and d[6] != "  " and d[7] != "  " and d[8] != "  ":

                        print("Deu velha!")

                        break

                else:

                    print("Número inválido!")

                    continue

            else:

                print()

                print("Digite somente um número!")

                continue

        else:

            print()

            print("Digite somente números!")

            continue
