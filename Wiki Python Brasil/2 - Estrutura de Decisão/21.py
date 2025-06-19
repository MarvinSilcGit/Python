import math

valor = float(input("Digite o valor que deseja sacar: "))

valor_pagamento = math.trunc(valor)

if valor_pagamento < 10:

    print("Valor insuficiente para saque")

else:

    cedulas = 0

    limite_cedula = 100

    while True:

        if limite_cedula <= valor_pagamento:

            valor_pagamento -= limite_cedula

            cedulas += 1

        else:

            print(f"{cedulas} cédula(s) de R$ {limite_cedula:.2f}")

            if valor_pagamento == 0:

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