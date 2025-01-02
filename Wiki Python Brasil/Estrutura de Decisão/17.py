anoBissexto = int(input("Digite o ano para saber se é bissexto ou não: "))

if anoBissexto % 4 == 0:

    if anoBissexto % 100 != 0:

        print("O ano %d é bissexto" % anoBissexto)

    elif anoBissexto % 100 == 0:

        print("O ano %d é bissexto especial" % anoBissexto)

else:

    print("O ano %d não é bissexto" % anoBissexto)