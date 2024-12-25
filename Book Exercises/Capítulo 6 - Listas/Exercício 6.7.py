x = list(input("Digite a expressão de parênteses: "))

z = 0

b = 0

e = 0

g = []

while z != len(x):

    if x[z] == "(":

        b += 1

        g.append(0)

    elif x[z] == ")":

        e += 1

        if len(g) == 0:

            break

        g.pop(-1)

    z += 1

while True:

    if(x[0]) == ")":

        print("Expressão incorreta")

        break

    if len(g) > 0:

        print("Expressão incorreta")

        break

    elif len(g) == 0:

        if b != e:

            print("Expressão incorreta")

            break

        else:

            print("Expressão correta")

            break
