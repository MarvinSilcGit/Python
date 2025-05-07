metragem = float(input("Digite a metragem: "))

cobertura_tinta = 3

metragem_lata = 18 * cobertura_tinta

quantidade_latas = 0

preco_final = 0

preco_lata = 80

if metragem / metragem_lata <= 1:

    quantidade_latas = 1

    preco_final = quantidade_latas * preco_lata

    print(f"Será necessária, no máximo, uma lata de tinta para pintar {metragem:.1f} metros². O custo será R$ {preco_final:.2f}")

else:

    if metragem % metragem_lata == 0:

        quantidade_latas = metragem / metragem_lata

        preco_final = quantidade_latas * preco_lata

        print(f"Serão necessária exatas {quantidade_latas:.0f} latas de tinta para pintar {metragem:.1f} metros². O custo será R$ {preco_final:.2f}")

    else:

        quantidade_latas = (metragem // metragem_lata) + 1

        preco_final = quantidade_latas * preco_lata

        print(f"Será necessária aos menos {quantidade_latas:.0f} latas de tinta para pintar {metragem:.1f} metros². O custo será R$ {preco_final:.2f}")