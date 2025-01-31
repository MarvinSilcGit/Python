#How to import: from Functions.Calculadoras.Uso_Geral import resto_divisao or import *


def atm_machine (valor_pagamento: float):

    if valor_pagamento < 1:

        return "Valor insuficiente para saque"

    else:

        cedulas = 0

        limite_cedula = 200

        resultado = []

        limite_moeda = 0.5

        moedas = 0

        while True:

            if limite_cedula <= valor_pagamento:

                valor_pagamento -= limite_cedula

                cedulas += 1

            else:

                resultado.append("%d cédula(s) de R$ %.2f" % (cedulas, limite_cedula))

                if valor_pagamento == 0:

                    return resultado

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

                    if 0 < valor_pagamento < 1:

                        if limite_moeda <= valor_pagamento:

                            valor_pagamento -= limite_moeda

                            moedas += 1

                            if valor_pagamento == 0:

                                resultado.append("%d moeda(s) de R$ %.2f" % (moedas, limite_moeda))

                                return resultado
# FIXME: fazer funcionar com moedas menores que 50 centavos
#Acessar Valores
"""for contador2 in range(1, 100):

    for contador in atm_machine(contador2):

        print(contador)

print(atm_machine(11.5))"""


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