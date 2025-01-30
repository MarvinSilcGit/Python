contador1 = 1

while contador1 != 0:

    deposito_inicial = float(input("Qual o valor do depósito inicial na conta? "))

    deposito_mensal = float(input("Qual o valor depositado mensalmente? "))

    taxa_juros = float(input("Qual a taxa de juros anual da poupança no período? "))

    periodo = int(input("Digite a quantidade de meses do rendimento: "))

    print()

    ganho_total = deposito_inicial

    ganhoJuros = 0

    for contador2 in range(1, periodo + 1):

        ganho_total += ganho_total / 100 * taxa_juros / 12

        ganhoJuros += ganho_total / 100 * taxa_juros / 12

        print("O valor na conta no %d° mês era de %.2f. Com uma taxa de %.2f por cento, gerou o valor de R$ %.2f em juros" % (contador2, ganho_total, taxa_juros, ganhoJuros))

        ganho_total += deposito_mensal

    ganho_total = 0

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()