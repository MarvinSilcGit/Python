cont1 = 1

while cont1 != 0:

    raiz = float(input("Digite um número para saber a sua raiz aproximada, utilizando o método Newtoniano: "))

    base = 2

    produto = 0

    cont = 0

    produto = (base+(raiz/base))/2

    produto = produto*produto

    produto2 = produto*produto

    while cont <= produto:

        base = produto

        produto = (base+(raiz/base))/2

        if produto*produto-raiz <= 0.001:

            break

    print("A raiz aproximada de %d é: %.4f" % (raiz, produto))

    print()

    cont1 = int(input("Digite 0 para interromper a execução: "))

    print()
