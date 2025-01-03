valor = int(input("Digite um número: "))

quantidadeCentena = 0

quantidadeDezena = 0

quantidadeUnidade = 0

if valor // 100 > 0:

    quantidadeCentena = valor // 100

    valor -= quantidadeCentena * 100

    if valor // 10 > 0:

        quantidadeDezena = valor // 10

        valor -= quantidadeDezena * 10

        if valor // 1 > 0:

            quantidadeUnidade = valor // 1

            valor -= quantidadeUnidade * 1

print("%d = %d centenas, %d dezenas e %d unidades" % (0 + (quantidadeUnidade * 1) + 0 + (quantidadeDezena * 10) + 0 + (quantidadeCentena * 100),quantidadeCentena, quantidadeDezena, quantidadeUnidade))