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

        return "Cpf inválido"

    else:

        lista_estados = {0: "Bahia", 1: "Distrido Federal, Goiás, Mato Grosso do Sul ou Tocantins", 2: "Pará, Amazonas, Acre, Amapá, Rondônio ou Roraíma", 3: "Ceará, Maranhão ou Piauí",
                         4: "Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas", 5: "Bahia ou Sergipe", 6: "Minas Gerais", 7: "Rio de Janeiro ou Espírito Santo", 8: "São Paulo",
                         9 :"Paraná ou Santa Catarina"}

        resultado_posicao_j = 0

        resultado_posicao_k = 0

        contador = 10

        estado = int(cpf[8])

        for contador2 in range(9):

            resultado_posicao_j += int(cpf[contador2]) * contador

            contador -= 1

        if resultado_posicao_j % 11 < 2:

            posicao_j = 0

        elif 2 <= resultado_posicao_j % 11 <= 10: # equals to: elif resultado_posicao_j >= 2 and resultado_posicao_j <= 10

            posicao_j = 11 - (resultado_posicao_j % 11)

        else:

            return "Cpf inválido"

        contador = 11

        for contador2 in range(10):

            resultado_posicao_k += int(cpf[contador2]) * contador

            contador -= 1

        if resultado_posicao_k % 11 < 2:

            posicao_k = 0

        elif 2 <= resultado_posicao_k % 11 <= 10: # equals to: elif resultado_posicao_k >= 2 and resultado_posicao_k <= 10

            posicao_k = 11 - (resultado_posicao_k % 11)

        else:

            return "Cpf inválido"

        posicao_k = str(posicao_k)

        posicao_j = str(posicao_j)

        if posicao_j == cpf[9] and posicao_k == cpf[10]:

            for contador3 in range(14):

                cpf = list(cpf)

                if contador3 == 3:

                    cpf.insert(contador3, '.')

                elif contador3 == 7:

                    cpf.insert(contador3, '.')

                elif contador3 == 11:

                    cpf.insert(contador3, '-')

            cpf = ''.join(cpf)

            return f"O CPF {cpf} é válido, sendo emitido em: {lista_estados[estado]}"

        else:

            return "Cpf inválido"


def consumo_aparelho (volts: float, amperes: float):

    return f"Com uma voltagem de {volts:,.2f}v e {amperes:,.2f}A, a potência máxima será {volts * amperes:,.2f} Watts"


def formula_bhaskara (coeficiente_a, coeficiente_b, coeficiente_c):

    from fractions import Fraction

    if coeficiente_a == 0:

        return "Coeficiente a não pode ser 0"

    else:

        if coeficiente_a != 0 and coeficiente_b != 0 and coeficiente_c != 0:

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

                return f"Equação completa. A raiz positiva é {x_1}. A raiz negativa é {x_2:}"


print(formula_bhaskara(5, 7, 2))