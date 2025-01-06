numero1 = float(input("Digite o primeiro número: "))

numero2 = float(input("Digite o segundo número: "))

numero3 = float(input("Digite o terceiro número: "))

if numero1 > numero2 > numero3:

    print("%d\n%d\n%d" % (numero1, numero2, numero3))

elif numero1 > numero3 > numero2:

    print("%d\n%d\n%d" % (numero1, numero3, numero2))

elif numero2 > numero1 > numero3:

    print("%d\n%d\n%d" % (numero2, numero1, numero3))

elif numero2 > numero3 > numero1:

    print("%d\n%d\n%d" % (numero2, numero3, numero1))

elif numero3 > numero1 > numero2:

    print("%d\n%d\n%d" % (numero3, numero1, numero2))

elif numero3 > numero2 > numero1:

    print("%d\n%d\n%d" % (numero3, numero2, numero1))