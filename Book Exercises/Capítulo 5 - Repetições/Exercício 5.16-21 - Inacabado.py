contador1 = 1

while contador1 != 0:

    print()

    valor_pagamento = float(input("Digite o valor que deseja sacar: "))

    if valor_pagamento < 1:

        print("Valor insuficiente para saque")

        continue

    else:

        cedulas = 0

        limite_cedula = 200

        limite_moeda = 0.5

        moedas = 0

        while True:

            if limite_cedula <= valor_pagamento:

                valor_pagamento -= limite_cedula

                cedulas += 1

            else:

                print("%d cédula(s) de R$ %.2f" % (cedulas, limite_cedula))

                if valor_pagamento == 0:

                    break

                else:

                    if limite_cedula == 200:

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

                        limite_cedula = 2

                    elif limite_cedula == 2:

                        limite_cedula = 1

                    cedulas = 0

                    if valor_pagamento > 0 and valor_pagamento < 1:

                        if limite_moeda <= valor_pagamento:

                            valor_pagamento -= limite_moeda

                            moedas += 1

                            if valor_pagamento == 0:

                                print("%d moeda(s) de R$ %.2f" % (moedas, limite_moeda))

                                break

    print()

    contador1 = int(input("Digite 0 para interromper a execuão: "))