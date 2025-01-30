contador1 = 1

while contador1 != 0:

    total = 0

    codigo_produto = 1

    while codigo_produto != 0:

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

        codigo_produto = float(input("Digite o código do produto desejado: "))

        if codigo_produto == 0:

            print()

            print("O valor total das compras foi de R$ %.2f" % total)

            break

        else:

            quantidade_produto = int(input(f"Digite a quantidade desejada do produto {codigo_produto:.{0}f} "))

            if codigo_produto == 1:

                total += quantidade_produto * 0.5

            elif codigo_produto == 2:

                total += quantidade_produto * 1

            elif codigo_produto == 3:

                total += quantidade_produto * 4

            elif codigo_produto == 5:

                total += quantidade_produto * 7

            elif codigo_produto == 9:

                total += quantidade_produto * 8

            elif codigo_produto != 0 or codigo_produto != 1 or codigo_produto != 2 or codigo_produto != 3 or codigo_produto != 5 or codigo_produto != 9:

                print("Valor incorreto digitado")

                continue

            print("O valor atual das compras é R$ %.2f:" % total)

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))