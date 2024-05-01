tot = 0

estoq = {"alface": [1000, 2.30], "batata": [500, 1.20], "tomate": [1500, 2.30], "feijão": [600, 1.50]}

while True:

    c = 0

    print("*******************************")

    venda = input("Digite o produto desejado: ")

    if venda not in estoq:

        print("Digite somente itens disponíveis ")

        print("*******************************")

    else:

        print("Esse são os itens do estoque de %s: " % venda)

        print("%d unidade(s), a um preço de R$ %.2f" % (estoq[venda][0],estoq[venda][1]))

        print("*******************************")

        quat = int(input("Digite a quantidade à retirar do mesmo: "))

        if quat > estoq[venda][0]:

            print("A quantidade solicitada excede a capacidade do estoque")

        else:

            tot = quat*estoq[venda][1]

            c += tot

            estoq[venda][0]-=quat

            print("O valor da compra foi de: R$%.2f, com um total de: %.2f"%(tot,c))

            print("*******************************")

            print("A quantidade de %s agora é de %d"%(venda,estoq[venda][0]))
