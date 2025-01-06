produto1 = float(input("Digite o valor do primeiro produto: "))

produto2 = float(input("Digite o valor do primeiro produto: "))

produto3 = float(input("Digite o valor do primeiro produto: "))

if produto1 > produto2 > produto3:

    print("Você deve comprar o terceiro produto por ser o mais barato")

elif produto1 > produto3 > produto2:

    print("Você deve comprar o segundo produto por ser o mais barato")

elif produto2 > produto1 > produto3:

    print("Você deve comprar o terceiro produto por ser o mais barato")

elif produto2 > produto3 > produto1:

    print("Você deve comprar o primeiro produto por ser o mais barato")

elif produto3 > produto1 > produto2:

    print("Você deve comprar o segundo produto por ser o mais barato")

elif produto3 > produto2 > produto1:

    print("Você deve comprar o primeiro produto por ser o mais barato")