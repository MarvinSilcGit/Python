quantidade_litros = float(input("Digite a quantidade de litros: "))

tipo_gasolina = input("Para Álcool digite A\nPara Gasolina digite G\n")

preco_final = 0

if tipo_gasolina == "A" or tipo_gasolina == "a":

    if quantidade_litros <= 20:

        preco_final = quantidade_litros * 1.9

        preco_final -= preco_final / 100 * 3

    else:

        preco_final = quantidade_litros * 1.9

        preco_final -= preco_final / 100 * 4

elif tipo_gasolina == "G" or tipo_gasolina == "g":

    if quantidade_litros <= 20:

        preco_final = quantidade_litros * 2.5

        preco_final -= preco_final / 100 * 4

    else:

        preco_final = quantidade_litros * 2.5

        preco_final -= preco_final / 100 * 5

print("O preço final será R$ %.2f" % preco_final)