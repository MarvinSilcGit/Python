metragem = float(input("Digite a metragem: "))

print("Digite 0 para somente lata de 18 litros.\nDigite 1 para somentes galões de 3.6 litros.\nDigite 2 para uma combinação de ambos.")

resposta = input("?\n")

coberturaTinta = 6

metragemLata = 18 * coberturaTinta

precoLata = 80

metragemGalao = 3.6 * coberturaTinta

precoGalao = 25

quantidadeLatas = 0

precoFinal = 0

if resposta == "0":

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

elif resposta == "1":

    print(1)

elif resposta == "2":

    print(2)

else:

    print("Opção Inválida")