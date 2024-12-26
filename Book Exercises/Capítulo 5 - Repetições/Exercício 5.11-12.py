contador1 = 1

while contador1 != 0:

    depositoInicial = float(input("Qual o valor do depósito inicial na conta? "))

    depositoMensal = float(input("Qual o valor depositado mensalmente? "))

    taxaJuros = float(input("Qual a taxa de juros anual da poupança no período? "))

    periodo = int(input("Digite a quantidade de meses do rendimento: "))

    print()

    ganhoTotal = depositoInicial

    ganhoJuros = 0

    for contador2 in range(1, periodo + 1):

        ganhoTotal += ganhoTotal / 100 * taxaJuros / 12

        ganhoJuros += ganhoTotal / 100 * taxaJuros / 12

        print("O valor na conta no %d° mês era de %.2f. Com uma taxa de %.2f por cento, gerou o valor de R$ %.2f em juros" % (contador2, ganhoTotal, taxaJuros, ganhoJuros))

        ganhoTotal += depositoMensal

    ganhoTotal = 0

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()