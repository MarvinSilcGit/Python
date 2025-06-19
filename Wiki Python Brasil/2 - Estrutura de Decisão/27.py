quantidade_morango = float(input("Digite a quantidade em kilos de morangos: "))

quantidade_maca = float(input("Digite a quantidade em kilos de maçãs: "))

preco_final = 0

if quantidade_morango <= 5:

    preco_final += quantidade_morango * 2.5

else:

    preco_final += quantidade_morango * 2.2

if quantidade_maca <= 5:

    preco_final += quantidade_maca * 1.8

else:

    preco_final += quantidade_maca * 1.2

print(f"O preço final será R$ {preco_final}")