contador1 = 1

while contador1 != 0:

    numero = float(input("Digite um número para saber a sua raiz aproximada, utilizando o método Newtoniano: "))

    base = 2

    raizQuadrada = (base + numero / base) / 2

    raizQuadrada = raizQuadrada**2

    while raizQuadrada * raizQuadrada - numero > 0.001:

        base = raizQuadrada

        raizQuadrada = (base + numero / base) / 2

    print("A raiz aproximada de %d é: %.4f" % (numero, raizQuadrada))

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()