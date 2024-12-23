a = {}

x = 0

b = x

v = input("Digite a palavra para virar um dicionário: ")

while x != len(v):

    a[v[x]] = x

    print(a)

    x += 1

print(a)
