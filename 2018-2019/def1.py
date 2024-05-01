def pesquisa (l, valor):

    for x, e in enumerate(l):

        if e == valor:

            return x


lista = [10, 20, 25, 30]

print(pesquisa(lista, 24))
