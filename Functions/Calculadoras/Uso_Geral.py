#How to import: from Functions.Calculadoras.Uso_Geral import resto_divisao or import *

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


def raio_circulo (area: float):

    return 3.14 * (area ** 2)


def calculo_imc (peso: float, altura: float):

    return peso / altura ** 2


def calculo_tmb (peso: float, altura: float, idade: int, genero: str):

    lista_generos = ["Masculino", "masculino", "Feminino", "feminino"]

    if genero not in lista_generos:

        return "Gênero inválido"

    else:

        if genero == "Masculino" or genero == "masculino":

            taxa_metabolica_basal = (10 * peso) + (6.25 * altura) - (5 * idade) + 5

            return taxa_metabolica_basal

        elif genero == "Feminino" or genero == "feminino":

            taxa_metabolica_basal = (10 * peso) + (6.25 * altura) - (5 * idade) - 161

            return taxa_metabolica_basal


def juros_compostos (valor_inicial: float, aporte_mensal: float, juros_anual: float, quantidade_meses: int):

    ganho_bruto_total = valor_inicial

    ganho_juros = 0

    for contador in range(1, quantidade_meses + 1):

        ganho_bruto_total += ganho_bruto_total / 100 * juros_anual / 12

        ganho_juros += ganho_bruto_total / 100 * juros_anual / 12

        print("O valor no %d° mês será de R$ %.2f. Com uma taxa de %.2f por cento anual, gerou o valor de R$ %.2f em juros" % (contador, ganho_bruto_total, juros_anual, ganho_juros))

        ganho_bruto_total += aporte_mensal

    return ""