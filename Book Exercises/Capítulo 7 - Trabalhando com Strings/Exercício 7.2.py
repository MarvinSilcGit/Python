a = input("Digite a primeira string: ")

b = input("Digite a segunda string: ")

d = []

c = 0

for x in a:

    if x in b:

        d.append(x)

        c += 1

if c > 0:

    e = "".join(d)

    print("Os elemento iguais entre as duas strings são: %s"%e)

elif c == 0:

    print("Não há elementos iguais entre as duas strings")
