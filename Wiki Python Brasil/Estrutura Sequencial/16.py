metragem = float(input("Digite a metragem: "))

metragemLata = 18

quantidadeLatas = 0

precoFinal = 0

if metragem / metragemLata <= 1:

    quantidadeLatas = 1

    precoFinal = quantidadeLatas * 80

    print("Será necessária, no máximo, uma lata de tinta para pintar %.2f metros². O custo será R$ %.2f" % (metragem, precoFinal))

else:

    if metragem % metragemLata == 0:

        quantidadeLatas = metragem / metragemLata

        precoFinal = quantidadeLatas * 80

        print("Será necessária exatas %d latas de tinta para pintar %.2f metros². O custo será R$ %.2f" % (quantidadeLatas, metragem, precoFinal))

    else:

        quantidadeLatas = metragem / metragemLata + 1

        precoFinal = quantidadeLatas * 80

        print("Será necessária aos menos %d latas de tinta para pintar %.2f metros². O custo será R$ %.2f" % (quantidadeLatas, metragem, precoFinal))