tipoCedulas = [2, 5, 10, 20, 50, 100, 200]

while True:

    print()

    valorSaque = input("Digite o valor: ")

    print()

    if valorSaque.isdigit() == False:

        print("Digite somente números!")

        continue

    elif valorSaque == "0" or valorSaque == "3" or valorSaque == "1":

        print("Digite somente valores válidos")

        continue

    elif valorSaque[0] == "0":

        print("Números começando por 0 não são válidos!")

        continue

    else:

        a = 0

        y = []

        z = []

        p = 0

        w = len(tipoCedulas)-1

        tot = int(valorSaque)

        while w != -1:

            if tipoCedulas[w]+p <= tot:

                if tipoCedulas[w]+p+1 == tot:

                    if a != 0:

                        z.append(a)

                        y.append(tipoCedulas[w])

                    w -= 1

                    a= 0

                elif tipoCedulas[w]+p+3 == tot:

                    if a != 0:

                        z.append(a)

                        y.append(tipoCedulas[w])

                    w -= 1

                    a = 0

                else:

                    p += tipoCedulas[w]

                    a += 1

            else:

                if a != 0:

                    z.append(a)

                    y.append(tipoCedulas[w])

                a = 0

                w -= 1

                if p == tot:

                    w =- 1

                    a = 0

                    while a != len(z):

                        print("%d cédula(s) de R$ %d" % (z[a], y[a]))

                        a += 1