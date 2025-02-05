def binary_decimal (numero: str):

    tamanho_decimal = len(numero)

    decimal = 0

    expoente = tamanho_decimal - 1

    for contador in numero:

        if contador == "1":

            decimal += (2 ** expoente)

        elif contador == "0":

            decimal += 0

        else:

            return 'Esse número não é binário'

        expoente -= 1

        numero = int(numero)

    return f"{decimal}"


def decimal_binary (numero: int):

    resto = []

    numero_decimal = numero

    while numero_decimal != 0:

        resto.insert(0, str(numero_decimal % 2))

        numero_decimal = numero_decimal // 2

    resto = ''.join(resto)

    resto = int(resto)

    return f"{resto}"


def numero_algarismo_romano (numero: int):

    numero_romano = []

    limite_romano = 1000

    while numero != 0:

        if limite_romano <= numero:

            numero -= limite_romano

        else:

            numero_romano.append(limite_romano)

            if numero == 0:

                return numero_romano

            if limite_romano == 1000:

                limite_romano = 100

            elif limite_romano == 100:

                limite_romano = 50

            elif limite_romano == 50:

                limite_romano = 10

            elif limite_romano == 10:

                limite_romano = 1

    return numero_romano

print(numero_algarismo_romano(100))