contador = 1

while contador != 0:

    valorInicial = float(input("Qual o valor inicial da dívida? "))

    juros = float(input("Qual o juros mensal? "))

    valorPagoMensal = float(input("Qual o valor a ser pago mensalmente? "))

    div = 0

    cont = 1

    pmeses = valorPagoMensal

    meses = (valorInicial / 100) * juros

    if valorPagoMensal == juros:

        print()

        print("Efetue o pagamento de um valor maior. ")

        print()

        continue

    while valorPagoMensal < valorInicial:

        valorPagoMensal += pmeses

        valorInicial += meses

        cont = cont+1

    div = valorPagoMensal - valorInicial

    juros = juros*cont

    print()

    print("A dívida foi paga em %d meses, com um total de: %2.2f R$. Contendo um juros total de %.0f por cento " % (cont, valorPagoMensal, juros))

    print("Sendo amortizados %2.2f R$ na próxima fatura, por ter ultrapassado o valor da dívida" % div)

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()
