numero1 = float(input("Digite o primeiro número: "))

numero2 = float(input("Digite o segundo número: "))

numero3 = float(input("Digite o terceiro número: "))

if numero1 > numero2 > numero3:

    print("O primeiro número é o maior")

elif numero1 > numero3 > numero2:

    print("O primeiro número é o maior")

elif numero2 > numero1 > numero3:

    print("O segundo número é o maior")

elif numero2 > numero3 > numero1:

    print("O segundo número é o maior")

elif numero3 > numero1 > numero2:

    print("O terceiro número é o maior")

elif numero3 > numero2 > numero1:

    print("O terceiro número é o maior")