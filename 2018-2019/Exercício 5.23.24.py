cont = 0

while True:

    print()

    primo = int(input("Digite um número para saber se ele é primo ou não: "))

    if primo % 2 == 0 and primo != 2:

        print()

        print("O número %d não é primo" % primo)

        continue

    if primo == 2:

        cont = cont+1

    else:

        primos = (primo % 2)

        cont += 1

    print()

    print("%d é um número primo" % primo)
