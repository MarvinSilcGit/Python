metragem = float(input("Digite a metragem: "))

coberturaTinta = 3

metragemLata = 18 * coberturaTinta

quantidadeLatas = 0

precoFinal = 0

precoLata = 80

if metragem / metragemLata <= 1:

    quantidadeLatas = 1

    precoFinal = quantidadeLatas * precoLata

    print("Será necessária, no máximo, uma lata de tinta para pintar %.2f metros². O custo será R$ %.2f" % (metragem, precoFinal))

else:

    if metragem % metragemLata == 0:

        quantidadeLatas = metragem / metragemLata

        precoFinal = quantidadeLatas * precoLata

        print("Será necessária exatas %d latas de tinta para pintar %.2f metros². O custo será R$ %.2f" % (quantidadeLatas, metragem, precoFinal))

    else:

        quantidadeLatas = (metragem // metragemLata) + 1

        precoFinal = quantidadeLatas * precoLata

        print("Será necessária aos menos %d latas de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, metragem, precoFinal))