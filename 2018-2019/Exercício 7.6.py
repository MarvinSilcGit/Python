a = list(input("Digite a primeira string: "))

b = list(input("Digite a segunda string: "))

c = list(input("Digite a terceira string: "))

x = 0

z = 0

while z < len(b):

    if b[z] == a[x]:

        del a[x]

    x += 1

    if x == len(a):

        x = 0

        z += 1

    if z == len(b):

        for y in c:

            a.append(y)

        print(a)
