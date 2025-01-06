contador = 1

maiorTemperatura = 0

menorTemperatura = 0

while contador != 0:

    temperatura = float(input("Digite uma temperatura ou 0 para interromper a execução: "))

    if temperatura == 0:

        contador = 0

    else:

        if menorTemperatura == 0:

            menorTemperatura = temperatura

        if maiorTemperatura < temperatura:

            maiorTemperatura = temperatura

        if menorTemperatura > temperatura:

            menorTemperatura = temperatura

if maiorTemperatura == menorTemperatura:

    print("Os números são idênticos")

else:

    print("O maior temperatura foi %.1f° e a menor temperatura foi %.1f°" % (maiorTemperatura, menorTemperatura))