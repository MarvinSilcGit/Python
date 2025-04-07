from fractions import Fraction

from Functions.Calculadoras.Numbers import raiz_quadrada

from Functions.Calculadoras.Validations import validade_numero_decimal

coeficiente_a = int(input("Digite o valor do coeficiente a: "))

if coeficiente_a == 0:

    print("Coeficiente a não pode ser 0")

else:

    coeficiente_b = int(input("Digite o valor do coeficiente b: "))

    coeficiente_c = int(input("Digite o valor do coeficiente c: "))

    delta = coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c

    if delta < 0:

        print("A equação não possui raízes reais")

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

            print(f"A equação possui apenas uma raiz real. A raiz positiva é {x_1}")

        else:

            print(f"Equação completa. A raiz positiva é {x_1}. A raiz negativa é {x_2}")