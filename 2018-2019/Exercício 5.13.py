cont1 = 1

while cont1 != 0:

    valori = float(input("Qual o valor inicial da dívida? "))

    juros = float(input("Qual o juros mensal? "))

    vpago = float(input("Qual o valor a ser pago mensalmente? "))

    div = 0

    cont = 1

    pmeses = vpago

    meses = (valori/100)*juros

    if vpago == juros:

        print()

        print("Efetue o pagamento de um valor maior. ")

        print()

        continue

    while vpago < valori:

        vpago += pmeses

        valori += meses

        cont = cont+1

    div = vpago-valori

    juros = juros*cont

    print()

    print("A dívida foi paga em %d meses, com um total de: %2.2f R$. Contendo um juros total de %.0f por cento " % (cont, vpago, juros))

    print("Sendo amortizados %2.2f R$ na próxima fatura, por ter ultrapassado o valor da dívida" % div)

    print()

    cont1 = int(input("Digite 0 para interromper a execução: "))

    print()
