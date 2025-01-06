quantidadeFile = int(input("Digite a quantidade em kilos de Filé Duplo: "))

quantidadePicanha = int(input("Digite a quantidade em kilos de Picanha: "))

quantidadeAlcatra = int(input("Digite a quantidade em kilos de Alcatra: "))

precoFinal = 0

if quantidadeFile <= 5:

    precoFinal += quantidadeFile * 4.9

else:

    precoFinal += quantidadeFile * 5.8

if quantidadePicanha <= 5:

    precoFinal += quantidadePicanha * 5.9

else:

    precoFinal += quantidadePicanha * 6.8

if quantidadeAlcatra <= 5:

    precoFinal += quantidadeAlcatra * 6.9

else:

    precoFinal += quantidadePicanha * 7.8

print("O preço final será R$ %.2f" % precoFinal)