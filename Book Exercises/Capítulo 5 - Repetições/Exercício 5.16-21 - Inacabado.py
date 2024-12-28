contador1 = 1

while contador1 != 0:

    print()
#Imprimir quantas cédulas são necessárias para pagar; sempre priorizando a cédulas e moedas de maoir valor;

    valor = float(input("Digite o valor a pagar: "))

    cedulas = 0

    atual = 100

    apagar = valor

    moeda = 0

    while True:

        if atual <= apagar:

            apagar -= atual

            cedulas += 1

        else:

            print("%d cédula(s) de R$ %.2f" % (cedulas, atual))

            if apagar == 0:

                break

            elif atual == 100:

                atual = 50

            elif atual == 50:

                atual = 20

            elif atual == 20:

                atual = 10

            elif atual == 10:

                atual = 5

            elif atual == 5:

                atual = 1

            elif atual == 1:

                atual = 0.50

                moeda += 1

                print("%d moeda(s) de R$ %1.2f centavos" % (moeda, atual))

                cedulas = 0

            """elif atual == 0.50:

                atual = 0.10

                moeda =+ 1

                print("%d moeda(s) de R$ %1.2f centavos" % (moeda, atual))

                cedulas = 0

            elif atual == 0.10:

                atual = 0.05

                moeda =+ 1

                print("%d moeda(s) de R$ %1.2f centavos" % (moeda, atual))

                cedulas = 0

            elif atual == 0.05:

                atual = 0.02

                moeda =+ 1

                print("%d moeda(s) de R$ %1.2f centavos" % (moeda, atual))

                cedulas = 0

            elif atual == 0.02:

                atual = 0.01

                moeda =+ 1

                print("%d moeda(s) de R$ %1.2f centavos" % (moeda, atual))

                cedulas = 0

            elif atual == 0.01:

                atual = 0.01

                moeda =+ 1

                print("%d moeda(s) de R$ %1.2f centavos" % (moeda, atual))

                cedulas = 0"""

            cedulas = 0

    print()

    contador1 = int(input("Digite 0 para interromper a execuão: "))