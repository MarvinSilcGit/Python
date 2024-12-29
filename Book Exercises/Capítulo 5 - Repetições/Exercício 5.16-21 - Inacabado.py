contador1 = 1

while contador1 != 0:

    print()

    valorSaque = float(input("Digite o valor que deseja sacar: "))

    cedulas = 0

    limite_cedula = 100

    valorRetirada = valorSaque

    #moeda = 0

    while True:

        if limite_cedula <= valorRetirada:

            valorRetirada -= limite_cedula

            cedulas += 1

        else:

            print("%d cédula(s) de R$ %.2f" % (cedulas, limite_cedula))

            if valorRetirada == 0:

                break

            elif limite_cedula == 200:

                limite_cedula = 100

            elif limite_cedula == 100:

                limite_cedula = 50

            elif limite_cedula == 50:

                limite_cedula = 20

            elif limite_cedula == 20:

                limite_cedula = 10

            elif limite_cedula == 10:

                limite_cedula = 5

            elif limite_cedula == 5:

                limite_cedula = 1

            """elif atual == 1:

                atual = 0.50

                #moeda += 1

                print("%d moeda(s) de R$ %1.2f centavos" % (moeda, atual))

                cedulas = 0

            elif atual == 0.50:

                atual = 0.10

                moeda =+ 1

                print("%d moeda(s) de R$ %1.2f centavos" % (moeda, atual))

                cedulas = 0

            elif atual == 0.10:

                atual = 0.05

                moeda =+ 1

                print("%d moeda(s) de R$ %1.2f centavos" % (moeda, atual))

                cedulas = 0

            elif atual == 0.05:

                atual = 0.02

                moeda =+ 1

                print("%d moeda(s) de R$ %1.2f centavos" % (moeda, atual))

                cedulas = 0

            elif atual == 0.02:

                atual = 0.01

                moeda =+ 1

                print("%d moeda(s) de R$ %1.2f centavos" % (moeda, atual))

                cedulas = 0

            elif atual == 0.01:

                atual = 0.01

                moeda =+ 1

                print("%d moeda(s) de R$ %1.2f centavos" % (moeda, atual))

                cedulas = 0"""

            cedulas = 0

    print()

    contador1 = int(input("Digite 0 para interromper a execuão: "))