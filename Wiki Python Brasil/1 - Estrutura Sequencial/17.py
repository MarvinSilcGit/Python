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

        print(f"Serão necessários exatos {quantidade_galoes:.0f} galões de tinta para pintar {metragem_area:.2f} metros². O custo será R$ {preco_final:.2f}")

    else:

        quantidade_galoes = metragem_area // metragem_galao + 1

        preco_final = quantidade_galoes * preco_galao

        print(f"Serão necessários aos menos {quantidade_galoes:.0f} galões de tinta para pintar {metragem_area:.2f} metros². O custo será R$ {preco_final:.2f}")

else:

    if metragem_area % metragem_lata == 0:

        quantidade_latas = metragem_area / metragem_lata

        preco_final = quantidade_latas * preco_lata

        print(f"Serão necessária exatas {quantidade_latas:.0f} latas de tinta para pintar {metragem_area:.2f} metros². O custo será R$ {preco_final:.2f}")

    else:

        if metragem_area - metragem_lata < 0:

            quantidade_latas = metragem_area // metragem_lata + 1

            preco_final = quantidade_latas * preco_lata

            print(f"Serão necessária ao menos {quantidade_latas:.0f} latas de tinta para pintar {metragem_area:.2f} metros². O custo será R$ {preco_final:.2f}")

        else:

            quantidade_latas = metragem_area // metragem_lata

            preco_final = quantidade_latas * preco_lata

            metragemRestante = metragem_area - (metragem_lata * quantidade_latas)

            if metragemRestante % metragem_galao == 0:

                quantidade_galoes = metragemRestante / metragem_galao

                preco_final += quantidade_galoes * preco_galao

                print(f"Serão necessárias ao menos {quantidade_latas:.0f} latas de tinta e ao menos {quantidade_galoes:.0f} Galões para pintar {metragem_area:.2f} metros². O custo será {preco_final:.2f}")

            else:

                if metragemRestante // metragem_galao >= 4:

                    quantidade_latas +=1

                    preco_final = quantidade_latas * preco_lata

                    quantidade_galoes = 0

                else:

                    quantidade_galoes = metragemRestante // metragem_galao + 1

                    preco_final += quantidade_galoes * preco_galao

                print(f"Serão necessárias ao menos {quantidade_latas:.0f} latas de tinta e ao menos {quantidade_galoes:.0f} Galões para pintar {metragem_area:.2f} metros². O custo será R$ {preco_final:.2f}")