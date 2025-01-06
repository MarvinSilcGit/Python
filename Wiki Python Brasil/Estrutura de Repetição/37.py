contador = 1

codigo = 0

maiorAltura = 0

menorAltura = 0

maiorPeso = 0

menorPeso = 0

mediaAltura = 0

mediaPeso = 0

codigoPessoaMenorAltura = 0

codigoPessoaMaiorAltura = 0

codigoPessoaMaiorPeso = 0

codigoPessoaMenorPeso = 0

while contador != 0:

    altura = float(input("Digite a altura da pessoa: "))

    peso = float(input("Digite o peso da pessoa: "))

    codigo = int(input("Digite o código da pessoa: "))

    mediaAltura += altura

    mediaPeso += peso

    contador += 1

    if altura > maiorAltura:

        maiorAltura = altura

        menorAltura = altura

        codigoPessoaMaiorAltura = codigo

    if altura < menorAltura:

        menorAltura = altura

        codigoPessoaMenorAltura = codigo

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()

print("O cliente com o código %d teve a maior altura %.2f" % (codigoPessoaMaiorAltura, maiorAltura))

print("O cliente com o código %d teve a menor altura %.2f" % (codigoPessoaMenorAltura, menorAltura))