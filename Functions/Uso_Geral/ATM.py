from Functions.Calculadoras.Validations import validade_numero_decimal


def atm_machine (valor_pagamento: int):

    if validade_numero_decimal(valor_pagamento):

        return 'Valores não podem ser decimais'

    else:

        cedulas = 0

        limite_cedula = [200, 100, 50, 20, 10, 5, 2, 1]

        resultado = {}

        while valor_pagamento != 0:

            for contador in limite_cedula:

                if valor_pagamento >= contador:

                    valor_pagamento -= contador

                    cedulas += 1

                    resultado.update({cedulas: contador})

                    print(resultado)

                    cedulas = 0

                    print(cedulas)

        return resultado

print(atm_machine(120))