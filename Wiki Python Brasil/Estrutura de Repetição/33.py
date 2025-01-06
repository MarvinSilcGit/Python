contador = 1

maior_temperatura = 0

menor_temperatura = 0

while contador != 0:

    numero = float(input("Digite uma temperatura ou 0 para interromper a execução: "))

    if numero == 0:

        contador = 0

    else:

        if numero > maior_temperatura:

            maior_temperatura = numero


        if numero < menor_temperatura:

            menor_temperatura = numero

print("O maior temperatura foi %.1f° e a menor temperatura foi %.1f°" % (maior_temperatura, menor_temperatura))