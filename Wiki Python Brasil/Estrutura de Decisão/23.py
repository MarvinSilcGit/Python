import math

numeroDecimal = float(input("Digite o número para saber se é decimal ou não: "))

numeroInteiro = math.trunc(numeroDecimal)

if numeroDecimal > numeroInteiro:

    print("O número %.1f é decimal" % numeroDecimal)

else:

    print("O número %d não é decimal" % numeroInteiro)