numero1 = int(input("digite o primeiro número: "))

numero2 = int(input("digite o segundo número: "))

numero3 = int(input("digite o terceiro número: "))

if numero1 > numero2 > numero3:

    print("%d, %d" % (numero1, numero3))

if numero1 > numero3 > numero2:

    print("%d, %d" % (numero1, numero2))

if numero2 > numero1 > numero3:

    print("%d, s%d" % (numero2, numero3))

if numero2 > numero3 > numero1:

    print("%d, r%d" % (numero2, numero1))

if numero3 > numero2 > numero1:

    print("%d, t%d" % (numero3, numero1))

if numero3 > numero1 > numero2:

    print("%d, u%d" % (numero1, numero2))
