def pesquisa(l, valor):

    if valor in lista:

        return valor

    else:

        return "O valor procurado não foi encontrado"


lista = [10, 20, 25, 30]

print(pesquisa(lista,1))
