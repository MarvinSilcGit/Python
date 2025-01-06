ano_bissexto = int(input("Digite o ano para saber se é bissexto ou não: "))

if ano_bissexto % 4 == 0:

    if ano_bissexto % 100 != 0:

        print("O ano %d é bissexto" % ano_bissexto)

    elif ano_bissexto % 100 == 0:

        print("O ano %d é bissexto especial" % ano_bissexto)

else:

    print("O ano %d não é bissexto" % ano_bissexto)