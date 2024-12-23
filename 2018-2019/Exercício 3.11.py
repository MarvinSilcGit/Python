precoMercadoria = float(input("Digite o preço da mercadoria: "))

desconto = float(input("Digite a pocentagem de desconto: "))

valordesconto = (desconto / 10 ) * (precoMercadoria / 10)

precototal = precoMercadoria - valordesconto

print("O valor do desconto é de R$%.2f. E o preço à pagar é de R$ %.2f" % (valordesconto, precototal))