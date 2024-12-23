cont = 1

while cont != 0:

    print()

    a = input("Digite a lado de um quadrado: ")

    if a.isdigit():

        a = int(a)

        z = 0

        y = 0

        w = 0

        while y != a:

            while z != a:

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
