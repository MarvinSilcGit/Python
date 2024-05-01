p = input("Digite um texto: ")

a = input("Digite outro texto: ")

if p.isalpha() == True and a.isalpha() == True:

    if len(p) > len(a):

        d = p.find(a, 0)

        if d >= 0:

            print("a posição encontrada foi a partir da %d° posição" % d)

        else:

            print("A string %s não foi encontrada em %s" % (a, p))

    else:

        d = a.find(p, 0)

        if d >= 0:

            print("A posição encontrada foi a partir da %d° posição" % d)

        else:

            print("A string %s não foi encontrada em %s" % (p, a))

elif p.isalpha() == False and a.isalpha() == False:

    print("Não é permitido valores nulos")

elif p.isalpha() == False and a.isalpha() == True:

    print("Digite somente strings no dois campos")

elif p.isalpha() == True and a.isalpha() == False:

    print("Digite somente strings no dois campos")
