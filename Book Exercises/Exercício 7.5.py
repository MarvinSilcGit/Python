a = list(input("Digite a primeira string: "))

b = list(input("Digite a segunda string: "))

z = 0

x = 0

while z < len(b):

    if b[z] == a[x]:

        del a[x]

    x += 1

    if x == len(a):

        x = 0

        z += 1

c = "".join(a)

print(c)
