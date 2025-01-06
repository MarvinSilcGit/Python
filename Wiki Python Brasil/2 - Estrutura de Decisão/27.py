quantidadeMorango = float(input("Digite a quantidade em kilos de morangos: "))

quantidadeMaca = float(input("Digite a quantidade em kilos de maçãs: "))

precoFinal = 0

if quantidadeMorango <= 5:

    precoFinal += quantidadeMorango * 2.5

else:

    precoFinal += quantidadeMorango * 2.2

if quantidadeMaca <= 5:

    precoFinal += quantidadeMaca * 1.8

else:

    precoFinal += quantidadeMaca * 1.2

print("O preço final será R$ %.2f" % precoFinal)