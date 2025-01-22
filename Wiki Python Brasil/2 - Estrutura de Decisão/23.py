import math

numero = input("Digite o número para saber se é decimal ou não: ")

numero_decimal = float(numero)

numero_inteiro = math.trunc(numero_decimal)

if numero_decimal > numero_inteiro:

    print(f"O número {numero} é decimal")

else:

    if "." in numero:

        print(f"O número {numero} é decimal")

    else:

        print(f"O número {numero} não é decimal")