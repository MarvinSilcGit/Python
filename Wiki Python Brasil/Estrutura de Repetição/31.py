contador = 1

preco_final = 0

contador3 = 1

troco = 0

valor_pagamento = 0

while contador != 0:

    while True:

        print("Digite o preço da mercadoria %d ou 0 para finalizar a compra: " % contador3)

        preco = float(input(""))

        preco_final += preco

        contador3 += 1

        if preco == 0:

            contador3 = 1

            break

    print("Total: %.2f" % preco_final)

    while True:

        valor_pagamento = float(input("Digite o valor de pagamento: "))

        if valor_pagamento < preco_final:

            print("Valor insuficiente para o pagamento")

            continue

        else:

            troco = valor_pagamento - preco_final

            print("Troco: %.2f" % troco)

            break

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()