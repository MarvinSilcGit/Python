contador1 = 1

pagamentoMensal = 0

while contador1 != 0:

    valorInicial = float(input("Qual o valor inicial da dívida? "))

    jurosMensal = float(input("Qual o juros mensal? "))

    tempoPagamento = int(input("Qual será o número de parcelas? "))

    dividaTotal = valorInicial

    for contadorDivida in range(1, tempoPagamento + 1):

        dividaTotal += dividaTotal / 100 * jurosMensal

    pagamentoMensal = dividaTotal / tempoPagamento

    print()

    print("O pagamento da dívida de R$ %.2f foi feita em %d meses com um valor de R$ %.2f" % (dividaTotal, tempoPagamento, pagamentoMensal))

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    pagamentoMensal = 0

    dividaTotal = 0

    print()