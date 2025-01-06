def pesquisa_numero_lista (lista, valor):

    for x, e in enumerate(lista):

        if e == valor:

            return x

        else:

            return "O valor %d não está na lista %s" % (valor, lista)

lista = [10, 20, 25, 30]

print(pesquisa_numero_lista(lista, 24))
