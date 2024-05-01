def multiplo(x, w):

    x = int(x)

    w = int(w)

    b = 0

    if x > w:

        while True:

            if b*w == x:

                return"O número %s é múltiplo de %s" % (w, x)

            b += 1

            if b*w > x:

                return "O número %s não é múltiplo de %s" % (w, x)

    elif x < w:

        while True:

            if b*x == w:

                return "O número %s é múltiplo de %s" % (x, w)

            b += 1

            if b*x > w:

                return "O número %s não é múltiplo de %s" % (x, w)

    elif x == w:

        return "Valores equivalentes!"


while True:

    while True:

        print()

        x = input("Digite o primeiro número: ")

        if x.isdigit() == False:

            print()

            print("Digite somente números!")

            continue

        while True:

            print()

            w = input("Digite o segundo número: ")

            if w.isdigit() == False:

                print()

                print("Digite somente números!")

                continue

            print()

            print(multiplo(x, w))

            break
