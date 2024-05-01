def areat(b, a):

    b = int(b)

    a = int(a)

    b = (b*a)/2

    print()

    return "A área do trinângulo é %d²" % b


while True:

    while True:

        print()

        b=input("Digite a base do triângulo: ")

        if b.isdigit()==False:

            print()

            print("Digite somente números!")

            continue

        if b == "0" or b == "1":

            print()

            print("Número inválido!")

            continue

        while True:

            print()

            a = input("Digite a altura do triângulo: ")

            if a.isdigit() == False:

                print()

                print("Digite somente números!")

                continue

            if a == "0" or a == "1":

                print()

                print("Número inválido!")

                continue

            print(areat(b, a))

            break
