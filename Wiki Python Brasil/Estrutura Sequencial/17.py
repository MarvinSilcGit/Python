metragem = float(input("Digite a metragem: "))

coberturaTinta = 6

metragemLata = 18 * coberturaTinta

precoLata = 80

quantidadeLatas = 0

metragemGalao = 3.6 * coberturaTinta

precoGalao = 25

quantidadeGaloes = 0

precoFinal = 0

if metragem <= metragemGalao * 4:

    if metragem % metragemGalao == 0:

        quantidadeGaloes = metragem / metragemGalao

        precoFinal = quantidadeGaloes * precoGalao

        print("Serão necessários exatos %d galões de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeGaloes, metragem, precoFinal))

    else:

        quantidadeGaloes = (metragem // metragemGalao) + 1

        precoFinal = quantidadeGaloes * precoGalao

        print("Serão necessários aos menos %d galões de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeGaloes, metragem, precoFinal))

else:

    if metragem % metragemLata == 0:

        quantidadeLatas = metragem / metragemLata

        precoFinal = quantidadeLatas * precoLata

        print("Serão necessária exatas %d latas de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, metragem, precoFinal))

    else:

        if metragem - metragemLata < 0 or metragem - metragemLata > metragemGalao * 4:

            quantidadeLatas = metragem // metragemLata + 1

            precoFinal = quantidadeLatas * precoLata

            print("Serão necessária ao menos %d latas de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, metragem, precoFinal))

        else:

            quantidadeLatas = metragem // metragemLata

            precoFinal += quantidadeLatas * precoLata

            metragem = metragem % metragemLata

            if metragem % metragemGalao == 0:

                quantidadeGaloes = metragem / metragemGalao

                precoFinal += quantidadeGaloes * precoGalao

                print("Serão necessária ao menos %d latas de tinta e ao menos %d para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, quantidadeGaloes, metragem, precoFinal))

            else:

                print()