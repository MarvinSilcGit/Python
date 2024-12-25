a = list(input("Digite a primeira string: "))

b = list(input("Digite a segunda string: "))

d = []

f = 0

for x in a:

    if x not in b:

        d.append(x)

        break

    else:

        f += 1

for z in b:

    if z not in a:

        d.append(z)

        break

    else:

        f += 1

if f == len(a)+len(b):

    print("Todas as strings eram idênticas")

else:

    e = "".join(d)

    print(e)
