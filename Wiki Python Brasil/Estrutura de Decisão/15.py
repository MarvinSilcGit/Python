lado1 = int(input("Digite o primeiro lado do triângulo: "))

lado2 = int(input("Digite o segundo lado do triângulo: "))

lado3 = int(input("Digite o terceiro lado do triângulo: "))

if lado1 == 0 or lado2 == 0 or lado3 == 0:

    print("Um triângulo não poder lado 0")

else:

    if lado1 + lado2 <= lado3:

       print("A soma desses lados não forma um triângulo")

    else:

        if lado1 == lado2 == lado3:

            print("Esse é um triângulo equilátero")

        elif lado1 != lado2 != lado3 != lado1:

            print("Esse é um triângulo escaleno")

        elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:

            print("Esse é um triângulo isóceles")