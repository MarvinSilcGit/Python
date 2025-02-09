def juros_compostos (valor_inicial: float, aporte_mensal: float, juros_anual: float, quantidade_meses: int):

    ganho_bruto_total = valor_inicial

    ganho_juros = 0

    for contador in range(1, quantidade_meses + 1):

        ganho_bruto_total += ganho_bruto_total / 100 * juros_anual / 12

        ganho_juros += ganho_bruto_total / 100 * juros_anual / 12

        print("O valor no %d° mês será de R$ %.2f. Com uma taxa de %.2f por cento anual, gerou o valor de R$ %.2f em juros" % (contador, ganho_bruto_total, juros_anual, ganho_juros))

        ganho_bruto_total += aporte_mensal

    return ""