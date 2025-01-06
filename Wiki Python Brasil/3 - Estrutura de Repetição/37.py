contador = 1

contador2 = 0

codigo = 0

maior_altura = 0

menor_altura = 0

codigo_pessoa_menor_altura = 0

codigo_pessoa_maior_altura = 0

media_altura = 0

maior_peso = 0

menor_peso = 0

codigo_pessoa_maior_peso = 0

codigo_pessoa_menor_peso = 0

media_peso = 0

while contador != 0:

    altura = float(input("Digite a altura da pessoa: "))

    peso = float(input("Digite o peso da pessoa: "))

    codigo = int(input("Digite o código da pessoa: "))

    media_altura += altura

    media_peso += peso

    contador2 += 1

    if altura < 0.5 or peso < 30 or codigo < 1:

        print("Valores incorretos")

        continue

    else:

        if menor_altura == 0:

            menor_altura = altura

            codigo_pessoa_menor_altura = codigo

        if maior_altura < altura:

            maior_altura = altura

            codigo_pessoa_maior_altura = codigo

        if menor_altura > altura:

            menor_altura = altura

            codigo_pessoa_menor_altura = codigo

        if menor_peso == 0:

            menor_peso = peso

            codigo_pessoa_menor_peso = codigo

        if maior_peso < peso:

            maior_peso = peso

            codigo_pessoa_maior_peso = codigo

        if menor_peso > peso:

            menor_peso = peso

            codigo_pessoa_menor_peso = codigo

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()

media_altura = media_altura / contador2

media_peso = media_peso / contador2

print("O cliente com o código %d teve a maior altura %.2f" % (codigo_pessoa_maior_altura, maior_altura))

print("O cliente com o código %d teve a menor altura %.2f" % (codigo_pessoa_menor_altura, menor_altura))

print("A média de altura foi %.2f" % media_altura)

print()

print("O cliente com o código %d teve o maior peso %.1f" % (codigo_pessoa_maior_peso, maior_peso))

print("O cliente com o código %d teve o menor peso %.1f" % (codigo_pessoa_menor_peso, menor_peso))

print("A média de peso foi %.1f" % media_peso)