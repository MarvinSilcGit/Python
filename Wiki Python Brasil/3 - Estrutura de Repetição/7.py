numero_final = 0

for contador in range(5):

    numero = float(input("Digite um número: "))

    if numero > numero_final:

        numero_final = numero

print("O maior número foi %d" % numero_final)