contador = 0

while True:

    print()

    numeroPrimo = int(input("Digite um número inteiro para saber se ele é primo ou não: "))

    if numeroPrimo % 2 == 0 and numeroPrimo != 2:

        print()

        print("O número %d não é primo" % numeroPrimo)

        continue

    if numeroPrimo == 2:

        contador = contador + 1

    else:

        primos = (numeroPrimo % 2)

        contador += 1

    print()

    print("%d é um número primo" % numeroPrimo)
