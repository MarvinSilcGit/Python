import cmath

coeficiente_a = int(input("Digite o valor do coeficiente a: "))

if coeficiente_a < 1:

    print("Valor inválido")

else:

    coeficiente_b = int(input("Digite o valor do coeficiente b: "))

    coeficiente_c = int(input("Digite o valor do coeficiente c: "))

    delta = coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c

    x_1 = (- coeficiente_b - cmath.sqrt(delta)) / 2 * coeficiente_a

    x_2 = (- coeficiente_b + cmath.sqrt(delta)) / 2 * coeficiente_a

    x_1 = x_1.real

    x_2 = x_2.real

    if delta < 0:

        print("A equação não possui raizes reais")

    elif delta == 0:

        print("A equação possui apenas uma raiz real")

        print("A raiz positiva é %d" % x_2)

    else:

        print("A equação possui duas raiz reais")

        print("A raiz negativa é %d e a raiz positiva é %d" % (x_1, x_2))