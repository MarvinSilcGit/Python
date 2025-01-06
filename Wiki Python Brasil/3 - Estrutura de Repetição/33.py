contador = 1

maior_temperatura = 0

menor_temperatura = 0

while contador != 0:

    temperatura = float(input("Digite uma temperatura ou 0 para interromper a execução: "))

    if temperatura == 0:

        contador = 0

    else:

        if menor_temperatura == 0:

            menor_temperatura = temperatura

        if maior_temperatura < temperatura:

            maior_temperatura = temperatura

        if menor_temperatura > temperatura:

            menor_temperatura = temperatura

if maior_temperatura == menor_temperatura:

    print("Os números são idênticos")

else:

    print("O maior temperatura foi %.1f° e a menor temperatura foi %.1f°" % (maior_temperatura, menor_temperatura))