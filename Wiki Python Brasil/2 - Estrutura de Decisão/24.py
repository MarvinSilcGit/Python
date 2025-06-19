import math

operacao = input("Digite qual operação deseja realizar:\n1 - Inteiro ou decimal\n2 - Par ou Ímpar\n3 - Positivo ou Negativo\n")

if operacao == "1":

    numero_decimal = float(input("Digite o número para saber se é decimal ou não: "))

    numero_inteiro = math.trunc(numero_decimal)

    if numero_decimal > numero_inteiro:

        print(f"O número {numero_decimal} é decimal")

    else:

        print(f"O número {numero_inteiro} não é decimal")

elif operacao == "2":

    numero = int(input("Digite o número para saber se é par ou ímpar: "))

    if numero % 2 != 0:

        print(f"O número {numero} é ímpar")

    else:

        print(f"O número {numero} é par")

elif operacao == "3":

    numero = float(input("Digite o número para saber se é negativo ou positivo: "))

    if numero < 0:

        print(f"O número {numero:.1f} é negativo")

    else:

        print(f"O número {numero:.1f} é positivo")