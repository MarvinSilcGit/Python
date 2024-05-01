ced = [2, 5, 10, 20, 50, 100]

while True:

    print()

    valor = input("Digite o valor: ")

    print()

    if valor.isdigit() == False:

        print("Digite somente números!")

        continue

    elif valor == "0" or valor == "3" or valor == "1":

        print("Digite somente valores válidos")

        continue

    elif valor[0] == "0":

        print("Números começando por 0 não são válidos!")

        continue

    else:

        a = 0

        y = []

        z = []

        p = 0

        w = len(ced)-1

        tot = int(valor)

        while w != -1:

            if ced[w]+p <= tot:

                if ced[w]+p+1 == tot:

                    if a != 0:

                        z.append(a)

                        y.append(ced[w])

                    w -= 1

                    a= 0

                elif ced[w]+p+3 == tot:

                    if a != 0:

                        z.append(a)

                        y.append(ced[w])

                    w -= 1

                    a = 0

                else:

                    p += ced[w]

                    a += 1

            else:

                if a != 0:

                    z.append(a)

                    y.append(ced[w])

                a = 0

                w -= 1

                if p == tot:

                    w =- 1

                    a = 0

                    while a != len(z):

                        print("%d cédula(s) de R$ %d" % (z[a], y[a]))

                        a += 1

