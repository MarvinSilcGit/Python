import math

numero_decimal = float(input("Digite o número para saber se é decimal ou não: "))

numero_inteiro = math.trunc(numero_decimal)

if numero_decimal > numero_inteiro or numero_inteiro != numero_decimal:

    print("O número %.1f é decimal" % numero_decimal)

else:

    print("O número %d não é decimal" % numero_inteiro)

  #Update as below
"""    import math

    numero_decimal = numero

    numero_inteiro = math.trunc(numero_decimal)

    if numero_decimal > numero_inteiro:

        return "dd"

    else:

        numero_decimal = str(numero_decimal)

        if "." in numero_decimal:

            return True

        else:

            return False"""