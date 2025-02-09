#How to import: from Functions.Calculadoras.Uso_Geral import name_function

from Functions.Calculadoras.Numbers import raiz_quadrada

from Functions.Calculadoras.Validations import validade_numero_decimal


def raio_circulo (area: float):

    return 3.14 * (area ** 2)

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