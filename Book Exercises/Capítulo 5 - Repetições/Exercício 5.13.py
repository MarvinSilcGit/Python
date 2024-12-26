contador1 = 1

while contador1 != 0:

    valorInicial = float(input("Qual o valor inicial da dívida? "))

    jurosMensal = float(input("Qual o juros mensal? "))

    tempoPagamento = int(input("Qual será o número de parcelas? "))

    dividaTotal = valorInicial

    for contadorDivida in range(1, tempoPagamento + 1):

        dividaTotal += dividaTotal / 100 * jurosMensal


    print(dividaTotal)
    contador2 = 1

    pmeses = tempoPagamento

    meses = (valorInicial / 100) * jurosMensal

    if tempoPagamento == jurosMensal:

        print()

        print("Efetue o pagamento de um valor maior. ")

        print()

        continue

    while tempoPagamento < valorInicial:

        tempoPagamento += pmeses

        valorInicial += meses

        contador2 = contador2 + 1

    dividaTotal = tempoPagamento - valorInicial

    jurosMensal = jurosMensal * contador2

    print()

    print("A dívida foi paga em %d meses, com um total de: %2.2f R$. Contendo um juros total de %.0f por cento " % (contador2, tempoPagamento, jurosMensal))

    print("Sendo amortizados %2.2f R$ na próxima fatura, por ter ultrapassado o valor da dívida" % dividaTotal)

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()