popu = 0

soma = 0

mul = 12

cont = 0

adc = 0

ano = 0

cont2 = 1

final = 0

anos = 15

an = 1

while True:

    popu += 30+adc

    soma += mul*popu

    print("*******************************")

    print("População parcial da população foi de: %d" % popu)

    print("O resultado parcial %d:" % soma)

    cont += 1

    adc += anos

    if cont == 12*cont2:

        ano += 1

        cont2 += 1

        mul = mul+((mul/100)*5)

        print(mul)

        print("*******************************")

        print("O total foi %d com uma população de %d" % (soma, popu))

        if soma > 81000:

            soma = soma-((soma/100)*20)

            soma = soma+((soma/100)*9)

        else:

            soma = soma-((soma/100)*10)

        if soma > 4300000:

            soma = soma-((soma/100)*30)

            soma = soma+((soma/100)*9)

        print()

        print("Menos os tributos, o %d° ano ficou: %.2f" % (ano, soma))

        final += soma

        if ano == 2*an:

            anos += 100

            an += 1

        if ano == 2:

            break

print("A arrecadação final nos %d anos, foi de: %.2f" % (ano, final))
