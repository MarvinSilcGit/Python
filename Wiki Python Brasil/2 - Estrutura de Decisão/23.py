import math

numero_decimal = float(input("Digite o número para saber se é decimal ou não: "))

numero_inteiro = math.trunc(numero_decimal)

if numero_decimal > numero_inteiro:

    print("O número %.1f é decimal" % numero_decimal)

else:

    print("O número %d não é decimal" % numero_inteiro)