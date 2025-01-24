#How to import: from Functions.Matemáticas import resto_divisao or import *

from Functions.Matemáticas.Numbers import raiz_quadrada, numero_decimal_inteiro

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


def validade_cpf (cpf):

    if len(cpf) != 11:

        return "CPF inválido"

    else:

        dicionario_estados = {"0": "Bahia", "1": "Distrido Federal, Goiás, Mato Grosso do Sul ou Tocantins", "2": "Pará, Amazonas, Acre, Amapá, Rondônio ou Roraíma",
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

        cpf = list(cpf)

        if posicao_j == cpf[9] and posicao_k == cpf[10]:

            for contador3 in range(14):

                if contador3 == 3:

                    cpf.insert(contador3, '.')

                elif contador3 == 7:

                    cpf.insert(contador3, '.')

                elif contador3 == 11:

                    cpf.insert(contador3, '-')

            cpf = ''.join(cpf)

            return f"O CPF {cpf} é válido, sendo emitido em: {dicionario_estados[estado]}"

        else:

            return "CPF inválido"


def validade_cnpj(cnpj):

    if len(cnpj) != 12:

        return "CNPJ inválido. Digite somente os primeiros 12 digitos"

    else:

        resultado_posicao_x_1 = 0

        resultado_posicao_x_2 = 0

        contador = 5

        for contador2 in range(12):

            contador += 1

            resultado_posicao_x_1 += int(cnpj[contador2]) * contador

            if contador == 9:

                contador = 1

        cnpj = str(cnpj)

        cnpj += str(resultado_posicao_x_1 % 11)

        contador = 4

        for contador2 in range(13):

            contador += 1

            resultado_posicao_x_2 += int(cnpj[contador2]) * contador

            if contador == 9:

                contador = 1

        cnpj += str(resultado_posicao_x_2 % 11)

        cnpj = list(cnpj)

        for contador3 in range(18):

            if contador3 == 2:

                cnpj.insert(contador3, '.')

            elif contador3 == 6:

                cnpj.insert(contador3, '.')

            elif contador3 == 10:

                cnpj.insert(contador3, '/')

            elif contador3 == 15:

                cnpj.insert(contador3, '-')

        cnpj = ''.join(cnpj)

        return f"O CNPJ será {cnpj}"


def consumo_aparelho (volts: float, amperes: float):

    return f"Com uma voltagem de {volts:,.2f}v e {amperes:,.2f}A, a potência máxima será {volts * amperes:,.2f} Watts"


def equacao_segundo_grau_bhaskara (coeficiente_a: float, coeficiente_b: float, coeficiente_c: float):

    from fractions import Fraction

    if coeficiente_a == 0:

        return "Coeficiente a não pode ser 0"

    else:

        delta = coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c

        x_1 = -coeficiente_b + float(raiz_quadrada(delta))

        if numero_decimal_inteiro(x_1 / (2 * coeficiente_a)):

            x_1 = Fraction(int(x_1), int(2 * coeficiente_a))

        else:

            x_1 = x_1 / (2 * coeficiente_a)

        x_2 = -coeficiente_b - float(raiz_quadrada(delta))

        if numero_decimal_inteiro(x_2 / (2 * coeficiente_a)):

            x_2 = Fraction(int(x_2), int(2 * coeficiente_a))

        else:

            x_2 = x_2 / (2 * coeficiente_a)

        if delta < 0:

            return "A equação não possui raizes reais"

        elif delta == 0:

            return f"A equação possui apenas uma raiz real. A raiz positiva é {x_1}"

        else:

            return f"Equação completa. A raiz positiva é {x_1}. A raiz negativa é {x_2}"


def formatacao_numero_telefone (ddi: str, numero: str):

    dicionario_paises = {"55": "Brasil", "1": "Estados Unidos da America", "48": "Polônia"}

    numero_formatado = ddi

    numero_formatado += numero

    numero_formatado = list(numero_formatado)

    if ddi == "55":

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

                numero_formatado.insert(contador, '+')

            elif contador == 3:

                numero_formatado.insert(contador, ' ')

            elif contador == 4:

                numero_formatado.insert(contador, '(')

            elif contador == 7:

                numero_formatado.insert(contador, ')')

            elif contador == 8:

                numero_formatado.insert(contador, ' ')

            elif contador == 14:

                numero_formatado.insert(contador, '-')

        numero_formatado = ''.join(numero_formatado)

    return f"O número {numero_formatado} pertence ao país: {dicionario_paises[ddi]}. Mais precisamente: {dicionario_ddd_brasil[codigo_local]}"