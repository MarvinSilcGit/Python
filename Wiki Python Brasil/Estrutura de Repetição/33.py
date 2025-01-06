contador = 1

maior_temperatura = 0

menor_temperatura = 0

while contador != 0:

    numero = int(input("Digite uma temperatura ou 0 para interromper a execução: "))

    if numero == 0:

        contador = 0

    else:

        if numero > 1000:

            print("Valor inválido")

            continue

        else:

            if numero > maior_temperatura:

                maior_temperatura = numero

                menor_temperatura = numero

            if numero < menor_temperatura:

                menor_temperatura = numero

print("O maior número foi %d e o menor número foi %d" % (maior_temperatura, menor_temperatura))