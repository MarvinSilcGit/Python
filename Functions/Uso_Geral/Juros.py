def juros_compostos (valor_inicial: float, aporte_mensal: float, juros_anual: float, quantidade_meses: int):
    """Função que calcula juros compostos. Primeiro é o valor inicial, depois o aporte mensal, depois a taxa de juros anual, por fim a quantidade de meses que o dinheiro estará investido."""
    ganho_bruto_total = valor_inicial

    ganho_juros = 0

    for contador in range(1, quantidade_meses + 1):

        ganho_juros += ganho_bruto_total / 100 * juros_anual / 12

        ganho_bruto_total += ganho_bruto_total / 100 * juros_anual / 12

        print(f"O valor ao final do {contador}° mês será de R$ {ganho_bruto_total:,.2f}. Com uma taxa anual de {juros_anual:,.2f}%, gerou-se um valor de R$ {ganho_juros:,.2f} em juros")

        ganho_bruto_total += aporte_mensal

    return ""