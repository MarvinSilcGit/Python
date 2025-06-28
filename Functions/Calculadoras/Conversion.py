def binary_decimal (numero: str):
    """Função que converte número binário em número decimal."""
    try:

        numero = int(numero)

    except ValueError:

        return 'Somente números inteiros são permitidos'

    else:

        numero = str(numero)

        numero = list(numero)

        for cont in numero:

            if '2' == cont or '3' == cont or '4' == cont or '5' == cont or '6' == cont or '7' == cont or '8' == cont or '9' == cont:

                return 'Somente 0 ou 1'

        numero_decimal = 0

        expoente = len(numero) - 1

        for _ in numero:

            if _ == "1":

                numero_decimal += (2 ** expoente)

            elif _ == "0":

                numero_decimal += 0

            expoente -= 1

        return numero_decimal


def decimal_binary (numero: str):
    """Função que converte número decimal em número binário."""
    try:

        numero = int(numero)

    except ValueError:

        return 'Somente números inteiros são permitidos'

    else:

        numero_binario = []

        while numero != 0:

            numero_binario.insert(0, str(numero % 2))

            numero //= 2

        numero_binario = int(''.join(numero_binario))

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