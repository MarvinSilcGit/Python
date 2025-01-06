quantidade_file = int(input("Digite a quantidade em kilos de Filé Duplo: "))

quantidade_picanha = int(input("Digite a quantidade em kilos de Picanha: "))

quantidade_alcatra = int(input("Digite a quantidade em kilos de Alcatra: "))

preco_final = 0

if quantidade_file <= 5:

    preco_final += quantidade_file * 4.9

else:

    preco_final += quantidade_file * 5.8

if quantidade_picanha <= 5:

    preco_final += quantidade_picanha * 5.9

else:

    preco_final += quantidade_picanha * 6.8

if quantidade_alcatra <= 5:

    preco_final += quantidade_alcatra * 6.9

else:

    preco_final += quantidade_picanha * 7.8

print("O preço final será R$ %.2f" % preco_final)