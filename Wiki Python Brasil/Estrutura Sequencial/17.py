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
        print(0)
        print("Serão necessários exatos %d galões de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeGaloes, metragem, precoFinal))

    else:

        quantidadeGaloes = (metragem // metragemGalao) + 1

        precoFinal = quantidadeGaloes * precoGalao
        print(1)
        print("Serão necessários aos menos %d galões de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeGaloes, metragem, precoFinal))

else:

    if metragem / metragemLata <= 1:

        quantidadeLatas = 1

        precoFinal = quantidadeLatas * precoLata
        print(2)
        print("Será necessária, no máximo, uma lata de tinta para pintar %.1f metros². O custo será R$ %.2f" % (metragem, precoFinal))

    else:

        if metragem % metragemLata == 0:

            quantidadeLatas = metragem / metragemLata

            precoFinal = quantidadeLatas * precoLata

            print(3)

            print("Serão necessária exatas %d latas de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, metragem, precoFinal))

        else:

            if (metragem - metragemLata) <= metragemGalao * 4:

                quantidadeLatas = metragem // metragemLata

                if metragem % metragemGalao == 0:

                    quantidadeGaloes = (metragem / metragemGalao)

                    precoFinal += quantidadeGaloes * precoGalao
                    print(4)
                    print("Serão necessários exatos %d galões de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeGaloes, metragem, precoFinal))

                else:

                    quantidadeGaloes = (metragem // metragemGalao) + 1


                    precoFinal = quantidadeGaloes * precoGalao + quantidadeLatas * precoLata
                    print(5)
                    print("Serão necessários aos %d latões de tinta e ao menos %d galões de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, quantidadeGaloes, metragem, precoFinal))

            else:

                quantidadeLatas = (metragem // metragemLata) + 1

                precoFinal = quantidadeLatas * precoLata

                print(6)

                print("Serão necessária aos menos %d latas de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, metragem, precoFinal))