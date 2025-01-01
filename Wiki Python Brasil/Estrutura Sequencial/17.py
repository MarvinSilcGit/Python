metragemArea = float(input("Digite a metragem: "))

coberturaTinta = 6

metragemLata = 18 * coberturaTinta

precoLata = 80

quantidadeLatas = 0

metragemGalao = 3.6 * coberturaTinta

precoGalao = 25

quantidadeGaloes = 0

precoFinal = 0

if metragemArea <= metragemGalao * 4:

    if metragemArea % metragemGalao == 0:

        quantidadeGaloes = metragemArea / metragemGalao

        precoFinal = quantidadeGaloes * precoGalao

        print("Serão necessários exatos %d galões de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeGaloes, metragemArea, precoFinal))

    else:

        quantidadeGaloes = metragemArea // metragemGalao + 1

        precoFinal = quantidadeGaloes * precoGalao

        print("Serão necessários aos menos %d galões de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeGaloes, metragemArea, precoFinal))

else:

    if metragemArea % metragemLata == 0:

        quantidadeLatas = metragemArea / metragemLata

        precoFinal = quantidadeLatas * precoLata

        print("Serão necessária exatas %d latas de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, metragemArea, precoFinal))

    else:

        if metragemArea - metragemLata < 0:

            quantidadeLatas = metragemArea // metragemLata + 1

            precoFinal = quantidadeLatas * precoLata

            print("Serão necessária ao menos %d latas de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, metragemArea, precoFinal))

        else:

            quantidadeLatas = metragemArea // metragemLata

            precoFinal = quantidadeLatas * precoLata

            metragemRestante = metragemArea - (metragemLata * quantidadeLatas)

            if metragemRestante % metragemGalao == 0:

                quantidadeGaloes = metragemRestante / metragemGalao

                precoFinal += quantidadeGaloes * precoGalao

                print("Serão necessárias ao menos %d latas de tinta e ao menos %d Galões para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, quantidadeGaloes, metragemArea, precoFinal))

            else:

                if metragemRestante // metragemGalao >= 4:

                    quantidadeLatas +=1

                    precoFinal = quantidadeLatas * precoLata

                    quantidadeGaloes = 0

                else:

                    quantidadeGaloes = metragemRestante // metragemGalao + 1

                    precoFinal += quantidadeGaloes * precoGalao

                print("Serão necessárias ao menos %d latas de tinta e ao menos %d Galões para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, quantidadeGaloes, metragemArea, precoFinal))