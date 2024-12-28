contador = 0

while True:

    print()

    numeroPrimo = int(input("Digite um número inteiro para saber se ele é primo ou não: "))

    if numeroPrimo == 0 or numeroPrimo == 1:

        print("Esse número é inválido")

        continue

    else:

        if numeroPrimo % 2 == 0 and numeroPrimo != 2:

            print()

            print("%d não é primo" % numeroPrimo)

            continue

        if numeroPrimo == 2:

            contador += 1

        print()

        print("%d é um número primo" % numeroPrimo)