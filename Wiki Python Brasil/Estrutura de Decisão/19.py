valor = int(input("Digite um número: "))

cedulas = 0

centena = 100

while True:

    if centena <= valor:

        valor -= centena

        cedulas += 1

    else:

        print("%d cédula(s) de R$ %.2f" % (cedulas, centena))

        if valor == 0:

            break

        else:

            if centena == 100:

                centena = 10

            elif centena == 10:

                centena = 1

            elif centena == 5:

                centena = 1

            cedulas = 0