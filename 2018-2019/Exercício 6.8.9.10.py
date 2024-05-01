L = [15, 7, 27, 39]

p = int(input("Digite o primeiro valor a procurar: "))

print("***********************************")

v = int(input("Digite o segundo valor a procurar: "))

x = 0

c = 0

z = 0

while z != len(L):

    if v == p:

        print("Digite valores distintos!")

        break

    print("***********************************")

    if L[z] == p:

        print("O valor %d foi encontrado na posição %d" % (p, z))

        x += 1

        if x == 1 and c < 1:

            print("O valor %d foi encontrado primeiro" % p)

    if L[z] == v:

        print("O valor %d foi encontrado na posição %d" % (v, z))

        c += 1

        if c == 1 and x < 1:

            print("O valor %d foi encontrado primeiro" % v)

    if L[z] != p:

        print("O valor %d não foi encontrado na posição %d" % (p, z))

    if L[z] != v:

        print("O valor %d não foi encontrado na posição %d" % (v, z))

    z += 1
