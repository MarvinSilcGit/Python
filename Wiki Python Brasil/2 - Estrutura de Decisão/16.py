import math

a = int(input("Digite o valor de a: "))

if a < 1:

    print("Valor inválido")

else:

    b = int(input("Digite o valor de b: "))

    c = int(input("Digite o valor de c: "))

    delta = b ** 2 - 4 * a * c

    print(math.sqrt(delta))

    raiz_negativa = (- b - math.sqrt(delta)) / 2 * a

    raiz_positiva = (- b + math.sqrt(delta)) / 2 * a

    print(raiz_negativa, raiz_positiva)