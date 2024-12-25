numero1 = int(input("digite o primeiro número: "))

numero2 = int(input("digite o segundo número: "))

numero3 = int(input("digite o terceiro número: "))

if numero1 > numero2 and numero2 > numero3:

    print("%d, %d, %d" % (numero1, numero2, numero3))

if numero1 < numero2 and numero2 < numero3:

          print("%d, %d, %d" % (numero3, numero2, numero1))

if numero1 > numero2 and numero2 < numero3 and numero3 > numero1:

          print("%d, %d, %d" % (numero3, numero1, numero2))

if numero1 > numero2 and numero2 < numero3 and numero3 < numero1:

          print("%d, %d, %d," % (numero1, numero3, numero2))

if numero1 < numero2 and numero2 > numero3 and numero3 > numero1:

          print("%d, %d, %d" % (numero2, numero3, numero1))

if numero1 < numero2 and numero2 > numero3 and numero3 < numero1:

          print("%d, %d, %d" % (numero2, numero1, numero3))
