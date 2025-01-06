metragem = float(input("Digite a metragem: "))

cobertura_tinta = 3

metragem_lata = 18 * cobertura_tinta

quantidade_latas = 0

preco_final = 0

preco_lata = 80

if metragem / metragem_lata <= 1:

    quantidade_latas = 1

    preco_final = quantidade_latas * preco_lata

    print("Será necessária, no máximo, uma lata de tinta para pintar %.2f metros². O custo será R$ %.2f" % (metragem, preco_final))

else:

    if metragem % metragem_lata == 0:

        quantidade_latas = metragem / metragem_lata

        preco_final = quantidade_latas * preco_lata

        print("Serão necessária exatas %d latas de tinta para pintar %.2f metros². O custo será R$ %.2f" % (quantidade_latas, metragem, preco_final))

    else:

        quantidade_latas = (metragem // metragem_lata) + 1

        preco_final = quantidade_latas * preco_lata

        print("Será necessária aos menos %d latas de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidade_latas, metragem, preco_final))