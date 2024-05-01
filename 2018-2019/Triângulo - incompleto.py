while True:

    while True:

        print()

        lado1 = input("Digite o lado A do trinângulo: ")

        if lado1.isdigit() == False:

            print()

            print("Digite somente números!")

            continue

        while True:

            print()

            lado2 = input("Digite o lado B do trinângulo: ")

            if lado2.isdigit() == False:

                print()

                print("Digite somente números!")

                continue

            while True:

                print()

                lado3 = input("Digite o lado C do trinângulo: ")

                if lado3.isdigit() == False:
                    print()

                    print("Digite somente números!")

                    continue

                a = "*"

                w = 1

                x = 0

                y = 0

                lado1 = int(lado1)

                lado2 = int(lado2)

                lado3 = int(lado3)

                z = lado3

                if lado2 - lado3 < lado1 < lado2 + lado3 and lado1 - lado3 < lado2 < lado1 + lado3 and lado1 - lado2 < lado3 < lado1 + lado2:

                    print()

                    print("Pode formar um triângulo")

                    print()

                    if lado1 == lado2 and lado2 == lado3:

                        print("O triângulo é equilátero")

                        print()

                    elif lado1 == lado2 and lado1 and lado2 != lado3 or lado1 == lado3 and lado1 and lado3 != lado2 or lado2 == lado3 and lado2 and lado3 != lado1:

                        print("O triângulo é isóceles")

                        print()

                    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:

                        print("O triângulo é escaleno")

                        print()

                    while True:

                        while x != z - 1:

                            print(end=" ")

                            x += 1

                        while y != 1:

                            print(a * w)

                            y += 1

                        y = 0

                        w += 1

                        x = 0

                        z -= 1

                        if w == lado3 + 1:

                            break

                    break

                else:

                    print()

                    print("Não pode formar um triângulo")

                    break

            break
