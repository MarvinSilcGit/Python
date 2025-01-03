while True:

    print()

    ladoQuadrado = input("Digite a lado de um quadrado: ")

    if ladoQuadrado.isdigit():

        ladoQuadrado = int(ladoQuadrado)

        z = 0

        y = 0

        w = 0

        while y != ladoQuadrado:

            while z != ladoQuadrado:

                z += 1

            while w != 1:

                w += 1

                print("*  "*z)

                z = 0

            w = 0

            y += 1

    else:

        print()

        print("Digite apenas números")

        continue