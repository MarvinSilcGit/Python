l3 = []

cont = 0

a = 1

print("Digite 0  para sair ")

print("*****************************")

while cont != 2:

    v1 = int(input("Digite o %d° número da primeira lista: " % a))

    if v1 == 0:

        break

    l3.append(v1)

    a += 1

print("Digite 0  para sair ")

a = 1

while cont != 2:

    v2 = int(input("Digite o %d° número da segunda lista: " % a))

    if v2 == 0:

        break

    l3.append(v2)

    a += 1

print(l3)

