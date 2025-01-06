quantidadeLitros = float(input("Digite a quantidade de litros: "))

tipoGasolina = input("Para Álcool digite A\nPara Gasolina digite G\n")

precoFinal = 0

if tipoGasolina == "A" or tipoGasolina == "a":

    if quantidadeLitros <= 20:

        precoFinal = quantidadeLitros * 1.9

        precoFinal -= precoFinal / 100 * 3

    else:

        precoFinal = quantidadeLitros * 1.9

        precoFinal -= precoFinal / 100 * 4

elif tipoGasolina == "G" or tipoGasolina == "g":

    if quantidadeLitros <= 20:

        precoFinal = quantidadeLitros * 2.5

        precoFinal -= precoFinal / 100 * 4

    else:

        precoFinal = quantidadeLitros * 2.5

        precoFinal -= precoFinal / 100 * 5

print("O preço final será R$ %.2f" % precoFinal)