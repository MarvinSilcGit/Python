precoMercadoria = float(input("Digite o preço da mercadoria: "))

desconto = int(input("Digite a pocentagem de desconto"))

valordesconto = (desconto/10)*(precoMercadoria/10)

precototal = precoMercadoria-desconto*10

print("O valor do desconto é de %.2f R$. E o preço à pagar é de %.2f R$" % (valordesconto, precototal))
