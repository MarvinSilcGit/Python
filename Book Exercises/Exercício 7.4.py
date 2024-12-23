a = input("Digite uma string: ")

b = []

d = 0

z = 0

for x in a:

    c = a.count(x)

    if x in b:

        d = x

    else:

        b.append(x)

        print("A string %s repete-se %d vez(es)" % (b[z], c))

        z += 1
