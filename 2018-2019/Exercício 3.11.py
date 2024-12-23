precoMercadoria = float(input("Digite o preço da mercadoria: "))

desconto = float(input("Digite a pocentagem de desconto: "))

valorDesconto = (desconto / 10 ) * (precoMercadoria / 10)

precoTotal = precoMercadoria - valorDesconto

print("O valor do desconto é de R$ %.2f. E o preço à pagar é de R$ %.2f" % (valorDesconto, precoTotal))