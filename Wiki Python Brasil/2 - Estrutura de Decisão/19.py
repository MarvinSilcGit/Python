valor = int(input("Digite um número: "))

quantidade_centenas = 0

quantidade_dezenas = 0

quantidade_unidades = 0

if valor // 100 > 0:

    quantidade_centenas = valor // 100

    valor -= quantidade_centenas * 100

if valor // 10 > 0:

    quantidade_dezenas = valor // 10

    valor -= quantidade_dezenas * 10

if valor // 1 > 0:

    quantidade_unidades = valor // 1

    valor -= quantidade_unidades * 1

print(f"{0 + (quantidade_unidades * 1) + 0 + (quantidade_dezenas * 10) + 0 + (quantidade_centenas * 100)} = {quantidade_centenas} centenas, {quantidade_dezenas} dezenas e {quantidade_unidades} unidades")