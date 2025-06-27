def binary_decimal (numero: str):
    """Função que converte número binário em número decimal."""
    numero_decimal = 0

    expoente = len(numero) - 1

    for _ in numero:

        if _ == "1":

            numero_decimal += (2 ** expoente)

        else:

            numero_decimal += 0

        expoente -= 1

        try:

            numero = int(numero)

        except ValueError:

            return 'Somente números são permitidos'

        else:

            return numero_decimal


def decimal_binary (numero: int):
    """Função que converte número decimal em número binário."""
    numero_binario = []

    while numero != 0:

        try:

            numero_binario.insert(0, str(numero % 2))

        except TypeError:

            return 'Somente números são permitidos'

        else:

            numero = numero // 2

    numero_binario = ''.join(numero_binario)

    try:

        numero_binario = int(numero_binario)

    except ValueError:

        return 'Somente números inteiros'

    else:

        return numero_binario

#FIXME: terminar de consertar o código. Possivelmente, a abordagem utilizando o ATM não funciona
def numero_algarismo_romano (numero: int):

    numero_romano = []

    lista_numeros = [1000, 500, 100, 50, 10, 5, 1]

    contador = 0

    while numero != 0:

        if numero >= lista_numeros[contador]:

            numero -= lista_numeros[contador]

            numero_romano.append(lista_numeros[contador])

        else:

            contador += 1

    return numero_romano

#print(numero_algarismo_romano(900))