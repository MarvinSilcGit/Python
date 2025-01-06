valor = int(input("Digite um número: "))

quantidade_centena = 0

quantidade_dezena = 0

quantidade_unidade = 0

quantidade_decimo = 0

if valor // 100 > 0:

    quantidade_centena = valor // 100

    valor -= quantidade_centena * 100

    if valor // 10 > 0:

        quantidade_dezena = valor // 10

        valor -= quantidade_dezena * 10

        if valor // 1 > 0:

            quantidade_unidade = valor // 1

            valor -= quantidade_unidade * 1

print("%d = %d centenas, %d dezenas e %d unidades" % (0 + (quantidade_unidade * 1) + 0 + (quantidade_dezena * 10) + 0 + (quantidade_centena * 100), quantidade_centena, quantidade_dezena, quantidade_unidade))