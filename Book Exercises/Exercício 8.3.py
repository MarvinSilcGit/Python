def area(w):

    w = int(w)

    w = w*w

    print()

    return("A área do quadrado é %d" % w)


while True:

    print()

    w = input("Digite o lado do quadrado: ")

    if w.isdigit() == False:

        print()

        print("Digite somente números!")

        continue

    print(area(w))
