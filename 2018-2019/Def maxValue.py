def maxValue(c):

    return "O maior valor é %s" % c


y = 0

l = []

while True:

    print()

    x = 0

    z = 0

    s = 0

    z = input("Digite o valor %d; ou 0 para intorromper e saber o maior valor: " % (y+1))

    if z.isdigit() == True:

        z = int(z)

        l.append(z)

        y += 1

        if z == 0:

            del l[x-1]

            s = 0

            while x != len(l):

                if l[x] > l[s] or l[x] == l[s]:

                    del l[s]

                    if x > 0:

                        x -= 1

                x += 1

                if x == len(l):

                    x = 0

                    s = 1

                if len(l) == 1:

                    y = 0

                    c = l.pop(0)

                    break

            print(maxValue(c))

    else:

        print()

        print("Digite somente números!")

        continue
