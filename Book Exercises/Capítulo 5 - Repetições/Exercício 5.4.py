contador1 = 1

while contador1 != 0:

    valorInicial = int(input("Digite o valor inicial: "))

    if valorInicial != 1:

        print("Número incorreto")

        continue

    else:

        valorFinal = int(input("Digite o valor final: "))

        while valorInicial < valorFinal:

            print(valorInicial)

            valorInicial += 2

        print()

        contador1 = int(input("Digite 0 para interromper a execução: "))