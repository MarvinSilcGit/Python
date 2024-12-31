metragem = float(input("Digite a metragem: "))

print("Digite 0 para somente lata de 18 litros.\nDigite 1 para somentes galões de 3.6 litros.\nDigite 2 para uma combinação de ambos.")

resposta = input("Qual a opção? ")

coberturaTinta = 6

metragemLata = 18 * coberturaTinta

precoLata = 80

quantidadeLatas = 0

metragemGalao = 3.6 * coberturaTinta

precoGalao = 25

quantidadeGaloes = 0

precoFinal = 0

if resposta == "0":

    if metragem / metragemLata <= 1:

        quantidadeLatas = 1

        precoFinal = quantidadeLatas * precoLata

        print("Será necessária, no máximo, uma lata de tinta para pintar %.1f metros². O custo será R$ %.2f" % (metragem, precoFinal))

    else:

        if metragem % metragemLata == 0:

            quantidadeLatas = metragem / metragemLata

            precoFinal = quantidadeLatas * precoLata

            print("Serão necessária exatas %d latas de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, metragem, precoFinal))

        else:

            quantidadeLatas = (metragem // metragemLata) + 1

            precoFinal = quantidadeLatas * precoLata

            print("Será necessária aos menos %d latas de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeLatas, metragem, precoFinal))

elif resposta == "1":

    if metragem / metragemGalao <= 1:

        quantidadeGaloes = 1

        precoFinal = quantidadeGaloes * precoGalao

        print("Será necessária, no máximo, um galão de tinta para pintar %.1f metros². O custo será R$ %.2f" % (metragem, precoFinal))

    else:

        if metragem % metragemGalao == 0:

            quantidadeGaloes = metragem / metragemGalao

            precoFinal = quantidadeGaloes * precoGalao

            print("Serão necessários exatos %d galões de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeGaloes, metragem, precoFinal))

        else:

            quantidadeGaloes = (metragem // metragemGalao) + 1

            precoFinal = quantidadeGaloes * precoGalao

            print("Serão necessários aos menos %d galões de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidadeGaloes, metragem, precoFinal))

elif resposta == "2":

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

    print("Opção Inválida")