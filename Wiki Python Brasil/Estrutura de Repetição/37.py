contador = 1

maiorAltura = 0

menorAltura = 0

maiorPeso = 0

menorPeso = 0

mediaAltura = 0

mediaPeso = 0

codigoPessoa = 0

while contador != 0:

    altura = float(input("Digite a altura da pessoa: "))

    peso = float(input("Digite o peso da pessoa: "))

    mediaAltura += altura

    menorPeso += peso

    codigo = 0

    if altura == 0:

        contador = 0

    else:

        contador += 1

        if altura > maiorAltura:

            maiorAltura = altura

            menorAltura = altura

        if altura < menorAltura:

            menorAltura = altura

print("O maior temperatura foi %.1f° e a menor temperatura foi %.1f°" % (maiorAltura, menorAltura))