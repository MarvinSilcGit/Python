preco = float(input("Digite o preço da unidade do Pão: "))

for contador in range(1, 51):

    print("%d - R$ %.2f" % (contador, preco * contador))