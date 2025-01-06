import math

operacao = input("Digite qual operação deseja realizar:\n1 - Inteiro ou decimal\n2 - Par ou Ímpar\n3 - Positivo ou Negativo\n")

if operacao == "1":

    numero_decimal = float(input("Digite o número para saber se é decimal ou não: "))

    numero_inteiro = math.trunc(numero_decimal)

    if numero_decimal > numero_inteiro:

        print("O número %.1f é decimal" % numero_decimal)

    else:

        print("O número %d não é decimal" % numero_inteiro)

elif operacao == "2":

    numero = int(input("Digite o número para saber se é par ou ímpar: "))

    if numero % 2 != 0:

        print("O número %d é ímpar" % numero)

    else:

        print("O número %d é par" % numero)

elif operacao == "3":

    numero = float(input("Digite o número para saber se é negativo ou positivo: "))

    if numero < 0:

        print("O número %.1f é negativo" % numero)

    else:

        print("O número %.1f é positivo" % numero)