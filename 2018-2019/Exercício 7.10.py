cont = 1

while cont != 0:

    d = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]

    print()

    print("Essas são as posições correspondentes ao teclado numérico: ")

    print(" 7  |  8 |  9")

    print("---+---+---")

    print(" 4  |  5 |  6")

    print("---+---+---")

    print(" 1  |  2 |  3")

    print()

    nome1 = input("Digite o nome do 1° jogador: ")

    if nome1.isalnum() == True:

        print()

        nome2 = input("Digite o nome do 2° jogador: ")

        if nome2.isalnum() == True:

            while True:

                for a in "a":

                    while True:

                        print()

                        jog1 = input("Jogador %s, posição: " % nome1)

                        if jog1.isdigit() == True:

                            if len(jog1) == 1:

                                print()

                                if jog1 == "1":

                                    if d[0] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[0] = "x"

                                elif jog1 == "2":

                                    if d[1] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[1] = "x"

                                elif jog1 == "3":

                                    if d[2] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[2] = "x"

                                elif jog1 == "4":

                                    if d[3] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[3] = "x"

                                elif jog1 == "5":

                                    if d[4] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[4] = "x"

                                elif jog1 == "6":

                                    if d[5] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[5] = "x"

                                elif jog1 == "7":

                                    if d[6] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[6] = "x"

                                elif jog1 == "8":

                                    if d[7] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[7] = "x"

                                elif jog1 == "9":

                                    if d[8] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[8] = "x"

                                elif jog1 == "0":

                                    print("Número inválido!")

                                    continue

                                print(" %s  |  %s |  %s"% (d[6], d[7], d[8]))

                                print("---+---+---")

                                print(" %s  |  %s |  %s" % (d[3], d[4], d[5]))

                                print("---+---+---")

                                print(" %s  |  %s |  %s" % (d[0], d[1], d[2]))

                                break

                            else:

                                print()

                                print("Digite somente um número!")

                                continue

                        else:

                            print()

                            print("Digite somente números!")

                            continue

                print()

                if "x" in d[0] and "x" in d[1] and "x" in d[2]:

                    print("O jogador %s venceu" % nome1)

                    # break

                elif "x" in d[3] and "x" in d[4] and "x" in d[5]:

                    print("O jogador %s venceu" % nome1)

                    #break

                elif "x" in d[6] and "x" in d[7] and "x" in d[8]:

                    print("O jogador %s venceu" % nome1)

                 #   break

                elif "x" in d[0] and "x" in d[3] and "x" in d[6]:

                    print("O jogador %s venceu" % nome1)

                   # break

                elif "x" in d[1] and "x" in d[4] and "x" in d[7]:

                    print("O jogador %s venceu" % nome1)

                    # break

                elif "x" in d[2] and "x" in d[5] and "x" in d[8]:

                    print("O jogador %s venceu" % nome1)

                   # break

                elif "x" in d[0] and "x" in d[4] and "x" in d[8]:

                    print("O jogador %s venceu" % nome1)

                    # break

                elif "x" in d[2] and "x" in d[4] and "x" in d[6]:

                    print("O jogador %s venceu" % nome1)

                    # break

                if d[0] != "  " and d[1] != "  " and d[2] != "  " and d[3] != "  " and d[4] != "  " and d[5] != "  " and d[6] != "  " and d[7] != "  " and d[8] != "  ":

                    print()

                    print("Deu velha!")

                    break

                break

                for b in "b":

                    while True:

                        print()

                        jog2 = input("Jogador %s, posição: " % nome2)

                        if jog2.isdigit() == True:

                            if len(jog2) == 1:

                                print()

                                if jog2 == "1":

                                    if d[0] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[0] = "o"

                                elif jog2 == "2":

                                    if d[1] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[1] = "o"

                                elif jog2 == "3":

                                    if d[2] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[2] = "o"

                                elif jog2 == "4":

                                    if d[3] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[3] = "o"

                                elif jog2 == "5":

                                    if d[4] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[4] = "o"

                                elif jog2 == "6":

                                    if d[5] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[5] = "o"

                                elif jog2 == "7":

                                    if d[6] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[6] = "o"

                                elif jog2 == "8":

                                    if d[7]!="  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[7] = "o"

                                elif jog2 == "9":

                                    if d[8] != "  ":

                                        print("Local ocupado!")

                                        continue

                                    else:

                                        d[8] = "o"

                                elif jog2 == "0":

                                    print("Número inválido!")

                                    continue

                                print(" %s  |  %s |  %s" % (d[6],d[7],d[8]))

                                print("---+---+---")

                                print(" %s  |  %s |  %s" % (d[3],d[4],d[5]))

                                print("---+---+---")

                                print(" %s  |  %s |  %s" % (d[0],d[1],d[2]))

                                break

                            else:

                                print()

                                print("Digite somente um número!")

                                continue

                        else:

                            print()

                            print("Digite somente números!")

                            continue

                print()

                if "o" in d[0] and "o" in d[1] and "o" in d[2]:

                    print("O jogador %s venceu" % nome2)

                    break

                elif "o" in d[3] and "o" in d[4] and "o" in d[5]:

                    print("O jogador %s venceu" % nome2)

                    break

                elif "o" in d[6] and "o" in d[7] and "o" in d[8]:

                    print("O jogador %s venceu" % nome2)

                    break

                elif "o" in d[0] and "o" in d[3] and "o" in d[6]:

                    print("O jogador %s venceu" % nome2)

                    break

                elif "o" in d[1] and "o" in d[4] and "o" in d[7]:

                    print("O jogador %s venceu" % nome2)

                    break

                elif "o" in d[2] and "o" in d[5] and "o" in d[8]:

                    print("O jogador %s venceu" % nome2)

                    break

                elif "o" in d[0] and "o" in d[4] and "o" in d[8]:

                    print("O jogador %s venceu" % nome2)

                    break

                elif "o" in d[2] and "o" in d[4] and "o" in d[6]:

                    print("O jogador %s venceu" % nome2)

                    break

        else:

            print()

            print("Digite somente números e/ou letras para o nome do jogador!")

            continue

    else:

        print()

        print("Digite somente números e/ou letras para o nome do jogador!")

        continue
