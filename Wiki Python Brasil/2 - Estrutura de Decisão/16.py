import cmath

a = int(input("Digite o valor de a: "))

if a < 1:

    print("Valor inválido")

else:

    b = int(input("Digite o valor de b: "))

    c = int(input("Digite o valor de c: "))

    delta = b ** 2 - 4 * a * c

    raiz_negativa = (- b - cmath.sqrt(delta)) / 2 * a

    raiz_positiva = (- b + cmath.sqrt(delta)) / 2 * a

    raiz_negativa = raiz_negativa.real

    raiz_positiva = raiz_positiva.real

    if delta < 0:

        print("A equação não possui raizes reais")

    elif delta == 0:

        print("A equação possui apenas uma raiz real")

        print("A raiz positiva é %d" % raiz_positiva)

    else:

        print("A equação possui duas raiz reais")

        print("A raiz negativa é %d e a raiz positiva é %d" % (raiz_negativa, raiz_positiva))