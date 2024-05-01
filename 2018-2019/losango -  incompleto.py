cont = 1

while cont != 0:

    print("#############################")

    palavra = input("Digite a palavra: ")

    z = 0

    a = "*"

    b = 1

    y = 0

    w = 0

    s = len(palavra)

    if palavra.isalpha() == True:

        while True:

            while w < s-1:

                print(end=" ")

                w += 1

            while y < 1:

                print(a*b)

                b += 1

                y += 1

            s -= 1

            y = 0

            w = 0

            if s == 0:

                break

        b -= 1

        s = len(palavra)

        w = len(palavra)

        w -= 1

        while w != 0:

            while s > w:

                print(end=" ")

                s -= 1

            while y < 1:

                b -= 1

                print(a*b)

                y += 1

            y = 0

            w -= 1

            s = len(palavra)

    else:

        print("#############################")

        print("Digite apenas uma palavra simples")

    print("#############################")

    cont = int(input("Digite 0 para interromper o programa: "))
