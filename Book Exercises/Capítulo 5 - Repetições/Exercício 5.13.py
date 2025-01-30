contador1 = 1

pagamentoMensal = 0

while contador1 != 0:

    valor_inicial = float(input("Qual o valor inicial da dívida? "))

    juros_mensal = float(input("Qual o juros mensal? "))

    tempo_pagamento = int(input("Qual será o número de parcelas? "))

    divida_total = valor_inicial

    for contadorDivida in range(1, tempo_pagamento + 1):

        divida_total += divida_total / 100 * juros_mensal

    pagamentoMensal = divida_total / tempo_pagamento

    print()

    print("O pagamento da dívida de R$ %.2f foi feita em %d meses com um valor de R$ %.2f" % (divida_total, tempo_pagamento, pagamentoMensal))

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    pagamentoMensal = 0

    divida_total = 0

    print()