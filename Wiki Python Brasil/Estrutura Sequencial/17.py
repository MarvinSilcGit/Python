metragem_area = float(input("Digite a metragem: "))

cobertura_tinta = 6

metragem_lata = 18 * cobertura_tinta

preco_lata = 80

quantidade_latas = 0

metragem_galao = 3.6 * cobertura_tinta

preco_galao = 25

quantidade_galoes = 0

preco_final = 0

if metragem_area <= metragem_galao * 4:

    if metragem_area % metragem_galao == 0:

        quantidade_galoes = metragem_area / metragem_galao

        preco_final = quantidade_galoes * preco_galao

        print("Serão necessários exatos %d galões de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidade_galoes, metragem_area, preco_final))

    else:

        quantidade_galoes = metragem_area // metragem_galao + 1

        preco_final = quantidade_galoes * preco_galao

        print("Serão necessários aos menos %d galões de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidade_galoes, metragem_area, preco_final))

else:

    if metragem_area % metragem_lata == 0:

        quantidade_latas = metragem_area / metragem_lata

        preco_final = quantidade_latas * preco_lata

        print("Serão necessária exatas %d latas de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidade_latas, metragem_area, preco_final))

    else:

        if metragem_area - metragem_lata < 0:

            quantidade_latas = metragem_area // metragem_lata + 1

            preco_final = quantidade_latas * preco_lata

            print("Serão necessária ao menos %d latas de tinta para pintar %.1f metros². O custo será R$ %.2f" % (quantidade_latas, metragem_area, preco_final))

        else:

            quantidade_latas = metragem_area // metragem_lata

            preco_final = quantidade_latas * preco_lata

            metragemRestante = metragem_area - (metragem_lata * quantidade_latas)

            if metragemRestante % metragem_galao == 0:

                quantidade_galoes = metragemRestante / metragem_galao

                preco_final += quantidade_galoes * preco_galao

                print("Serão necessárias ao menos %d latas de tinta e ao menos %d Galões para pintar %.1f metros². O custo será R$ %.2f" % (quantidade_latas, quantidade_galoes, metragem_area, preco_final))

            else:

                if metragemRestante // metragem_galao >= 4:

                    quantidade_latas +=1

                    preco_final = quantidade_latas * preco_lata

                    quantidade_galoes = 0

                else:

                    quantidade_galoes = metragemRestante // metragem_galao + 1

                    preco_final += quantidade_galoes * preco_galao

                print("Serão necessárias ao menos %d latas de tinta e ao menos %d Galões para pintar %.1f metros². O custo será R$ %.2f" % (quantidade_latas, quantidade_galoes, metragem_area, preco_final))