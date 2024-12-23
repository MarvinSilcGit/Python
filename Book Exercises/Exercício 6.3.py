l3 = []

l1 = [5, 6, 7, 8, 9]

l2 = [0, 1, 2, 3, 4]

x = len(l1)

x2 = len(l2)

x2 -= 1

# Primeiro laço: para saber se há elementos iguais entre as listas;

while True:

    x -= 1

    if (l1[x]) == (l2[x2]):

        l1[x] = "*"

    if x == 0:

        x2 -= 1

        x = len(l1)

    if x2 < 0:

        break

x2 = len(l1)

x2 -= 1

x -= 1

# Segundo laço: para saber se há elementos iguais dentro da primeira lista;

while x != 0:

    x2 -= 1

    if (l1[x]) == (l1[x2]):

        l1[x] = "*"

    if x2 == 0:

        x -= 1

        x2 = x

# Terceiro laço: para saber se há elemento iguais dentro da segunda lista;

x = len(l1)

x2 = len(l2)

x -= 1

x2 -= 1

while x2 != 0:

    x -= 1

    if(l2[x2]) == (l2[x]):

        l2[x2] = "*"

    if x == 0:

        x2 -= 1

        x = x2

# Quarto laço: para saber se há elementos iguais entre as listas;

x = len(l1)

x2 = len(l2)

x -= 1

x2 -= 1

while True:

    l3.append(l1[x])

    l3.append(l2[x])

    x -= 1

    x2 -= 1

    if x < 0:

        break

print(l3)
