from Functions.Calculadoras.Validations import validade_numero_decimal


def resto_divisao (valor1: float, valor2: float):

    resto = 0

    if valor1 == 0 or valor2 == 0:

        return "Divisão por zero inválida"

    else:

        if valor1 == valor2:

            resto = 0

        elif valor1 > valor2:

            while valor2 + resto <= valor1:

                resto += valor2

            resto = valor1 - resto

        else:

            while valor1 + resto < valor2:

                resto += valor1

            while resto != valor2:

                resto += 1

        return "O resto da divisão entre %.1f e %.1f é: %.1f" % (valor1, valor2, resto)


def resto_inteiro_divisao (valor1: float, valor2: float):

    resto_inteiro = 0

    resto = 0

    if valor1 == 0 or valor2 == 0:

        return "Divisão por zero inválida"

    else:

        if valor1 == valor2:

            resto_inteiro = 1

        elif valor1 > valor2:

            while valor2 + resto <= valor1:

                resto_inteiro += 1

                resto += valor2

        else:

            while valor1 + resto < valor2:

                resto += valor1

            while resto != valor2:

                resto += 1

        return f"{resto_inteiro}"


def raiz_quadrada (numero: float):

    base = 2

    if numero < 0:

        return "número imaginário"

    resultado_raiz_quadrada = (base + numero / base) / 2

    resultado_raiz_quadrada **= 2

    while resultado_raiz_quadrada * resultado_raiz_quadrada - numero > 0.001:

        base = resultado_raiz_quadrada

        resultado_raiz_quadrada = (base + numero / base) / 2

    return f"{resultado_raiz_quadrada:,.4f}"


def calculo_fatorial (numero: int):

    resultado_fatorial = numero

    for contador in range(numero, 1, -1):

        resultado_fatorial *= contador - 1

    return f"{resultado_fatorial}"


def equacao_segundo_grau_bhaskara (coeficiente_a: float, coeficiente_b: float, coeficiente_c: float):

    from fractions import Fraction

    if coeficiente_a == 0:

        return "Coeficiente a não pode ser 0"

    else:

        delta = coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c

        if delta < 0:

            return "A equação não possui raízes reais"

        else:

            x_1 = -coeficiente_b + float(raiz_quadrada(delta))

            if validade_numero_decimal(x_1 / (2 * coeficiente_a)):

                x_1 = Fraction(int(x_1), int(2 * coeficiente_a))

            else:

                x_1 /= (2 * coeficiente_a)

            x_2 = -coeficiente_b - float(raiz_quadrada(delta))

            if validade_numero_decimal(x_2 / (2 * coeficiente_a)):

                x_2 = Fraction(int(x_2), int(2 * coeficiente_a))

            else:

                x_2 = x_2 / (2 * coeficiente_a)

            if delta == 0:

                return f"A equação possui apenas uma raiz real. A raiz positiva é {x_1}"

            else:

                return f"Equação completa. A raiz positiva é {x_1}. A raiz negativa é {x_2}"
#print(equacao_segundo_grau_bhaskara(3,-6, -8))

def calculo_porcentagem_representante (valor1: float, valor2: float):

    porcentagem = (valor1 / valor2) * 100

    return f'{valor1:,.2f} representa {porcentagem:,.2f}% de {valor2:,.2f}'