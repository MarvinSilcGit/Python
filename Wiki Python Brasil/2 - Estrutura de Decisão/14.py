nota_parcial1 = float(input("Digite a primeira nota parcial: "))

if nota_parcial1 > 10 or nota_parcial1 < 0:

    print("Nota inválida")

nota_parcial2 = float(input("Digite a segunda nota parcial: "))

if nota_parcial2 > 10 or nota_parcial2 < 0:

    print("Nota inválida")

media_final = (nota_parcial1 + nota_parcial2) / 2

if media_final >= 6:

    print("Aprovado e a média foi %.2f" % media_final)

    if media_final >= 9 and media_final <= 10:

        print("Conceito A")

    elif media_final >= 7.5 and media_final < 9:

        print("Conceito B")

    elif media_final >= 6 and media_final < 7.5:

        print("Conceito C")

else:

    print("Reprovado e a média foi %.2f" % media_final)

    if media_final >= 4 and media_final < 6:

        print("Conceito D")

    else:

        print("Conceito E")