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

        return "Gênero inválido"

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

                return "Esse é um triângulo isosceles"


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


def formatar_cpf (cpf: str):

    cpf = list(cpf)

    for contador in range(14):

        if contador == 3:

            cpf.insert(contador, '.')

        elif contador == 7:

            cpf.insert(contador, '.')

        elif contador == 11:

            cpf.insert(contador, '-')

    cpf = ''.join(cpf)

    return cpf


def validade_cpf (cpf):

    if len(cpf) != 11:

        return "CPF inválido"

    else:

        dicionario_estados = {"1": "Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins", "2": "Pará, Amazonas, Acre, Amapá, Rondônia ou Roraíma",
                              "3": "Ceará, Maranhão ou Piauí",
                              "4": "Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas", "5": "Bahia ou Sergipe", "6": "Minas Gerais",
                              "7": "Rio de Janeiro ou Espírito Santo", "8": "São Paulo",
                              "9":"Paraná ou Santa Catarina"}

        resultado_posicao_j = 0

        resultado_posicao_k = 0

        contador = 10

        estado = cpf[8]

        for contador2 in range(9):

            resultado_posicao_j += int(cpf[contador2]) * contador

            contador -= 1

        if resultado_posicao_j % 11 < 2:

            posicao_j = 0

        elif 2 <= resultado_posicao_j % 11 <= 10: # equals to: elif resultado_posicao_j >= 2 and resultado_posicao_j <= 10

            posicao_j = 11 - (resultado_posicao_j % 11)

        else:

            return "CPF inválido"

        contador = 11

        for contador2 in range(10):

            resultado_posicao_k += int(cpf[contador2]) * contador

            contador -= 1

        if resultado_posicao_k % 11 < 2:

            posicao_k = 0

        elif 2 <= resultado_posicao_k % 11 <= 10: # equals to: elif resultado_posicao_k >= 2 and resultado_posicao_k <= 10

            posicao_k = 11 - (resultado_posicao_k % 11)

        else:

            return "CPF inválido"

        posicao_k = str(posicao_k)

        posicao_j = str(posicao_j)

        if posicao_j == cpf[9] and posicao_k == cpf[10]:

            cpf = formatar_cpf(cpf)

            return f"O CPF {cpf} é válido, sendo emitido em {dicionario_estados[estado]}"

        else:

            return "CPF inválido"


def gerador_cpf ():

    import random as aleatoriedade

    cpf = []

    for contador in range(11):

        cpf.append(str(aleatoriedade.randint(0,9)))

    cpf = ''.join(cpf)

    cpf = formatar_cpf(cpf)

    return cpf


def formatar_cnpj (cnpj: str):

    cnpj = list(cnpj)

    for contador in range(18):

        if contador == 2:

            cnpj.insert(contador, '.')

        elif contador == 6:

            cnpj.insert(contador, '.')

        elif contador == 10:

            cnpj.insert(contador, '/')

        elif contador == 15:

            cnpj.insert(contador, '-')

    cnpj = ''.join(cnpj)

    return cnpj


def validade_cnpj(cnpj: str):

    cnpj_validador = list(cnpj[0:12])

    cnpj_validador = ''.join(cnpj_validador)

    resultado_posicao_x_1 = 0

    resultado_posicao_x_2 = 0

    contador = 5

    for contador2 in cnpj_validador:

        contador += 1

        posicao_x_1 = int(contador2)

        resultado_posicao_x_1 += posicao_x_1 * contador

        if contador == 9:

            contador = 1

    cnpj_validador += str(resultado_posicao_x_1 % 11)

    contador = 4

    for contador2 in cnpj_validador:

        contador += 1

        posicao_x_2 = int(contador2)

        resultado_posicao_x_2 += posicao_x_2 * contador

        if contador == 9:

            contador = 1

    cnpj_validador += str(resultado_posicao_x_2 % 11)

    cnpj_validador = formatar_cnpj(cnpj_validador)

    cnpj = formatar_cnpj(cnpj)

    if cnpj == cnpj_validador:

        return f"O CNPJ {cnpj} é válido"

    else:

        return f"O CNPJ {cnpj} é inválido"

print(validade_cnpj('59120772000100'))

def gerador_cnpj ():

    import random as aleatoriedade

    cnpj = ''

    for contador in range(14):

        if contador == 8 or contador == 9 or contador == 10:

            cnpj += '0'

        elif contador == 11:

            cnpj += '1'

        else:

            cnpj += (str(aleatoriedade.randint(0,9)))

    cnpj = formatar_cnpj(cnpj)

    return cnpj


def formatacao_numero_telefone (numero: str):

    numero_formatado = numero

    numero_formatado = list(numero_formatado)

    codigo_local = str(numero[0:2])

    dicionario_ddd_brasil = {"68": "Acre", "96": "Amapá", "92": "Amazonas", "97": "Amazonas", "91": "Pará", "93": "Pará", "94": "Pará",
                             "69": "Rondônia", "95": "Roraima", "63": "Tocantins", "61": "Distrito Federal", "62": "Goiás", "64": "Goiás",
                             "65": "Mato Grosso", "66": "Mato Grosso", "67": "Mato Grosso do Sul", "82": "Alagoas", "71": "Bahia", "73": "Bahia",
                             "74": "Bahia", "75": "Bahia", "77": "Bahia", "79": "Sergipe", "85": "Ceará", "88": "Ceará", "98": "Maranhão", "99": "Maranhão",
                             "83": "Paraíba", "81": "Pernambuco", "87": "Pernambuco", "86": "Piauí", "89": "Piauí", "84": "Rio Grande do Norte",
                             "27": "Espírito Santo", "28": "Espírito Santo", "31": "Minas Gerais", "32": "Minas Gerais", "33": "Minas Gerais",
                             "34": "Minas Gerais", "35": "Minas Gerais", "37": "Minas Gerais", "38": "Minas Gerais", "21": "Rio de Janeiro",
                             "22": "Rio de Janeiro", "24": "Rio de Janeiro", "11": "São Paulo", "12": "São Paulo", "13": "São Paulo", "14": "São Paulo",
                             "15": "São Paulo", "16": "São Paulo", "17": "São Paulo", "18": "São Paulo", "19": "São Paulo", "41": "Paraná", "42": "Paraná",
                             "43": "Paraná", "44": "Paraná", "45": "Paraná", "46": "Paraná", "51": "Rio Grande do Sul", "53": "Rio Grande do Sul",
                             "54": "Rio Grande do Sul", "55": "Rio Grande do Sul", "47": "Santa Catarina", "48": "Santa Catarina", "49": "Santa Catarina"}

    if len(numero) != 11:

        return 'Número inválido'

    if not codigo_local in dicionario_ddd_brasil:

        return "DDD inválido"

    for contador in range(17):

        if contador == 0:

            numero_formatado.insert(contador, '(')

        elif contador == 3:

            numero_formatado.insert(contador, ')')

        elif contador == 4:

            numero_formatado.insert(contador, ' ')

        elif contador == 7:

            numero_formatado.insert(contador, '')

        elif contador == 11:

            numero_formatado.insert(contador, '-')

    numero_formatado = ''.join(numero_formatado)

    return f"{numero_formatado}"