contador = 1

maior_numero = 0

menor_numero = 0

while contador != 0:

    numero = int(input("Digite um número ou 0 para interromper a execução: "))

    if numero == 0:

        contador = 0

    else:

        if numero > 1000:

            print("Valor inválido")

            continue

        else:

            if numero > maior_numero:

                maior_numero = numero

                menor_numero = numero

            if numero < menor_numero:

                menor_numero = numero

print("O maior número foi %d e o menor número foi %d" % (maior_numero, menor_numero))