ano_bissexto = int(input("Digite o ano para saber se é bissexto ou não: "))

if ano_bissexto % 4 == 0:

    if ano_bissexto % 100 != 0:

        print(f"O ano {ano_bissexto} é bissexto")

    elif ano_bissexto % 100 == 0:

        print(f"O ano {ano_bissexto} é bissexto especial")

else:

    print(f"O ano {ano_bissexto} não é bissexto")