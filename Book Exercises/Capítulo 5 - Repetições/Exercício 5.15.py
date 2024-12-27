contador1 = 1

while contador1 != 0:

    total = 0

    codigoProduto = 1

    while codigoProduto != 0:

        print()

        print("Se não deseja nenhum produto digite o valor 0")

        print()

        print("código 1, referente ao produto A; com valor de R$ 0,50")

        print()

        print("código 2, referente ao produto B; com valor de R$ 1,00")

        print()

        print("código 3, referente ao produto C; com valor de R$ 4,00")

        print()

        print("código 5, referente ao produto E, com valor de R$ 7,00")

        print()

        print("código 9, referente ao produto I; com valor de R$ 8,00")

        print()

        codigoProduto = float(input("Digite o código do produto desejado: "))

        if codigoProduto == 0:

            print()

            print("O valor total das compras foi de R$ %.2f" % total)

            break

        elif codigoProduto == 1:

            quantidadeProduto = int(input("Digite a quantidade desejada do produto A: "))

            total += quantidadeProduto * 0.5

        elif codigoProduto == 2:

            quantidadeProduto = int(input("Digite a quantidade desejada do produto B: "))

            total += quantidadeProduto * 1

        elif codigoProduto == 3:

            quantidadeProduto = int(input("Digite a quantidade desejada do produto C: "))

            total += quantidadeProduto * 4

        elif codigoProduto == 5:

            quantidadeProduto = int(input("Digite a quantidade desejada do produto E: "))

            total += quantidadeProduto * 7

        elif codigoProduto == 9:

            quantidadeProduto = int(input("Digite a quantidade desejada do produto I: "))

            total += quantidadeProduto * 8

        elif codigoProduto != 0 or codigoProduto != 1 or codigoProduto != 2 or codigoProduto != 3 or codigoProduto != 5 or codigoProduto != 9:

            print("Valor incorreto digitado")

            continue

        print("O valor atual das compras é R$ %.2f:" % total)

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))