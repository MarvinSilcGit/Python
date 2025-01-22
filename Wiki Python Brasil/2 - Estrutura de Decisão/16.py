import cmath

from fractions import Fraction

coeficiente_a = int(input("Digite o valor do coeficiente a: "))

if coeficiente_a == 0:

    print("Coeficiente a não pode ser 0")

else:

    coeficiente_b = int(input("Digite o valor do coeficiente b: "))

    coeficiente_c = int(input("Digite o valor do coeficiente c: "))

    delta = coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c

    x_1 = - coeficiente_b + cmath.sqrt(delta)

    x_2 = - coeficiente_b - cmath.sqrt(delta)

    x_1 = x_1.real

    x_2 = x_2.real

    x_1 = str(x_1)

    x_2 = str(x_2)


    if "." in x_1:

        x_1 = float(x_1)

        x_1 = Fraction(int(x_1), int(2 * coeficiente_a))

    else:

        x_1 = float(x_1)

        x_1 = x_1 / (2 * coeficiente_a)

    if "." in x_2:

        x_2 = float(x_2)

        x_2 = Fraction(int(x_2), int(2 * coeficiente_a))

    else:

        x_2 = float(x_2)

        x_2 = x_2 / (2 * coeficiente_a)

    if delta < 0:

        print("A equação não possui raizes reais")

    elif delta == 0:

        print(f"A equação possui apenas uma raiz real. A raiz positiva é {x_1}")

    else:

        print(f"Equação completa. A raiz positiva é {x_1}. A raiz negativa é {x_2}")