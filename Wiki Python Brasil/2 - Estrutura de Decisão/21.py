import math

valor = float(input("Digite o valor que deseja sacar: "))

valorPagamento = math.trunc(valor)

if valorPagamento < 10:

    print("Valor insuficiente para saque")

else:

    cedulas = 0

    limite_cedula = 100

    while True:

        if limite_cedula <= valorPagamento:

            valorPagamento -= limite_cedula

            cedulas += 1

        else:

            print("%d cédula(s) de R$ %.2f" % (cedulas, limite_cedula))

            if valorPagamento == 0:

                break

            else:

                if limite_cedula == 100:

                    limite_cedula = 50

                elif limite_cedula == 50:

                    limite_cedula = 20

                elif limite_cedula == 20:

                    limite_cedula = 10

                elif limite_cedula == 10:

                    limite_cedula = 5

                elif limite_cedula == 5:

                    limite_cedula = 2

                elif limite_cedula == 2:

                    limite_cedula = 1

                cedulas = 0