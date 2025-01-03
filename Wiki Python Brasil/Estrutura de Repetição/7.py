numeroFinal = 0

for contador in range(5):

    numero = float(input("Digite um número: "))

    if numero > numeroFinal:

        numeroFinal = numero

print("O maior número foi %d" % numeroFinal)