notaParcial1 = float(input("Digite a primeira nota parcial: "))

if notaParcial1 > 10 or notaParcial1 < 0:

    print("Nota inválida")

notaParcial2 = float(input("Digite a segunda nota parcial: "))

if notaParcial2 > 10 or notaParcial2 < 0:

    print("Nota inválida")

mediaFinal = (notaParcial1 + notaParcial2) / 2

if mediaFinal >= 6:

    print("Aprovado e a média foi %.2f" % mediaFinal)

    if mediaFinal >= 9 and mediaFinal <= 10:

        print("Conceito A")

    elif mediaFinal >= 7.5 and mediaFinal < 9:

        print("Conceito B")

    elif mediaFinal >= 6 and mediaFinal < 7.5:

        print("Conceito C")

else:

    print("Reprovado e a média foi %.2f" % mediaFinal)

    if mediaFinal >= 4 and mediaFinal < 6:

        print("Conceito D")

    else:

        print("Conceito E")