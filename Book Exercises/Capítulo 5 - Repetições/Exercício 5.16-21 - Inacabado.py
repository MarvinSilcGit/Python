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

            cedulas = 0

    print()

    contador1 = int(input("Digite 0 para interromper a execuão: "))