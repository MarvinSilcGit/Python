#How to import: from Functions.Matemáticas import resto_divisao or import *


def palindromo (valor):

    contador2 = 0

    if len(valor) <= 2:

        return "Tamanho insuficiente!"

    else:

        for contador1 in range(0, len(valor)):

            if valor[contador1] == valor[- 1 - contador1]:

                contador2 += 1

        if contador2 == len(valor):

            return "%s é palíndromo" % valor

        else:

            return "%s não é palíndromo" % valor


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

        return "Genêro inválido"

    else:

        if genero == "Masculino" or genero == "masculino":

            taxa_metabolica_basal = (10 * peso) + (6.25 * altura) - (5 * idade) + 5

            return taxa_metabolica_basal

        elif genero == "Feminino" or genero == "feminino":

            taxa_metabolica_basal = (10 * peso) + (6.25 * altura) - (5 * idade) - 161

            return taxa_metabolica_basal


def triangulo_validade_tipo (lado1: int, lado2: int, lado3: int):

    if lado1 == 0 or lado2 == 0 or lado3 == 0:

        return "Um triângulo não pode ter lado 0"

    else:

        if lado1 + lado2 <= lado3:

            return "A soma desses lados não forma um triângulo"

        else:

            if lado1 == lado2 == lado3:

                return "Esse é um triângulo equilátero"

            elif lado1 != lado2 != lado3 != lado1:

                return "Esse é um triângulo escaleno"

            elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:

                return "Esse é um triângulo isóceles"


def gerador_tabuada_simples (numero_tabuada: int):

    for contador in range(1, 10 + 1):

        print("%d x %d = %d " % (numero_tabuada, contador, numero_tabuada * contador))

    return 0


def gerador_tabuada_inicio_fim (numero_inicial: int, numero_final: int):

    for contador in range(1, numero_final + 1):

        print("%d x %d = %d " % (numero_inicial, contador, numero_inicial * contador))

    return 0


def gerador_tabuada_inicio_fim_razao (numero_inicial: int, numero_final: int, razao: int):

    for contador in range(1, numero_final + 1, razao):

        print("%d x %d = %d " % (numero_inicial, contador, numero_inicial * contador))

    return 0


def juros_compostos (valor_inicial: float, aporte_mensal: float, juros_anual: float, quantidade_meses: int):

    ganho_bruto_total = valor_inicial

    ganho_juros = 0

    for contador in range(1, quantidade_meses + 1):

        ganho_bruto_total += ganho_bruto_total / 100 * juros_anual / 12

        ganho_juros += ganho_bruto_total / 100 * juros_anual / 12

        print("O valor no %d° mês será de R$ %.2f. Com uma taxa de %.2f por cento anual, gerou o valor de R$ %.2f em juros" % (contador, ganho_bruto_total, juros_anual, ganho_juros))

        ganho_bruto_total += aporte_mensal

    return ""


def validade_cpf (valor):


    if len(valor) != 11:

        return "Cpf inválido"

    else:

        posicao_j = 0

        posicao_k = 0

        cpf = str(valor)

        estado = ""

        if cpf[8] == "0":

            estado = "Rio Grande do sul"

        elif cpf[8] == "1":

            estado = "Distrido Federal, Goiás, Mato Grosso do Sul ou Tocantins"

        elif cpf[8] == "2":

            estado = "Pará, Amazonas, Acre, Amapá, Rondônio ou Roraíma"

        elif cpf[8] == "3":

            estado = "Ceará, Maranhão ou Piauí"

        elif cpf[8] == "4":

            estado = "Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas"

        elif cpf[8] == "5":

            estado = "Bahia ou Sergipe"

        elif cpf[8] == "6":

            estado = "Minas Gerais"

        elif cpf[8] == "7":

            estado = "Rio de Janeiro ou Espírito Santo"

        elif cpf[8] == "8":

            estado = "São Paulo"

        elif cpf[8] == "9":

            estado = "Paraná ou Santa Catarina"

        else:

            return "cpf inválido"

        for contador in cpf:

            print(contador)

        return estado

print(validade_cpf('12348095523'))