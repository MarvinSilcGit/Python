contador = 1

precoFinal = 0

contador3 = 1

troco = 0

valorPagamento = 0

while contador != 0:

    while True:

        print("Digite o preço da mercadoria %d ou 0 para finalizar a compra: " % contador3)

        preco = float(input(""))

        precoFinal += preco

        contador3 += 1

        if preco == 0:

            contador3 = 1

            break

    print("Total: %.2f" % precoFinal)

    while True:

        valorPagamento = float(input("Digite o valor de pagamento: "))

        if valorPagamento < precoFinal:

            print("Valor insuficiente para o pagamento")

            continue

        else:

            troco = valorPagamento - precoFinal

            print("Troco: %.2f" % troco)

            break

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()