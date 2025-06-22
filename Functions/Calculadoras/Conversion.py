def binary_decimal (numero: str):

    numero_decimal = 0

    expoente = len(numero) - 1

    for _ in numero:

        if _ == "1":

            numero_decimal += (2 ** expoente)

        else:

            numero_decimal += 0

        expoente -= 1

        numero = int(numero)

    return f"{numero_decimal}"


def decimal_binary (numero: int):

    numero_binario = []

    while numero != 0:

        numero_binario.insert(0, str(numero % 2))

        numero = numero // 2

    numero_binario = ''.join(numero_binario)

    numero_binario = int(numero_binario)

    return f"{numero_binario}"

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