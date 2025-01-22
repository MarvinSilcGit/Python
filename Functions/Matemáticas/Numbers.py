def resto_divisao (valor1: float, valor2: float):

    resto = 0

    if valor1 == 0 or valor2 == 0:

        return "Divisão por zero inválida"

    else:

        if valor1 == valor2:

            resto = 0

        elif valor1 > valor2:

            while valor2 + resto <= valor1:

                resto += valor2

            resto = valor1 - resto

        else:

            while valor1 + resto < valor2:

                resto += valor1

            while resto != valor2:

                resto += 1

        return "O resto da divisão entre %.1f e %.1f é: %.1f" % (valor1, valor2, resto)


def resto_inteiro_divisao (valor1: float, valor2: float):

    resto_inteiro = 0

    resto = 0

    if valor1 == 0 or valor2 == 0:

        return "Divisão por zero inválida"

    else:

        if valor1 == valor2:

            resto_inteiro = 1

        elif valor1 > valor2:

            while valor2 + resto <= valor1:

                resto_inteiro += 1

                resto += valor2

        else:

            while valor1 + resto < valor2:

                resto += valor1

            while resto != valor2:

                resto += 1

        return f"{resto_inteiro}"


def raiz_quadrada (numero: float):

    base = 2

    if numero < 0:

        return "número imaginário"

    resultado_raiz_quadrada = (base + numero / base) / 2

    resultado_raiz_quadrada = resultado_raiz_quadrada ** 2

    while resultado_raiz_quadrada * resultado_raiz_quadrada - numero > 0.001:

        base = resultado_raiz_quadrada

        resultado_raiz_quadrada = (base + numero / base) / 2

    return f"{resultado_raiz_quadrada:,.4f}"


def numero_primo (numero: int):

    confirmacao = 2

    if numero == 0 or numero == 1:

        return "Esse número é inválido"

    if numero ==  2 or numero == 3:

        return "%d é um número primo" % numero

    else:

        for contador in range(confirmacao, numero + 1):

            if numero % contador != 0:

                confirmacao += 1

        if confirmacao == numero:

            return "%d é um número primo, pois é divisível somente por ele e por 1" % numero

        else:

            print("O número %d não é primo, pois ele é divisível por: " % numero, end="")

            for contador in range(1, numero + 1):

                if numero % contador == 0:

                    if numero - contador == 0:

                        print(contador, end=" ")

                    else:

                        print(contador, end=", ")
            return ""


def numero_par_impar (numero: int):

    if numero % 2 == 0:

        return "O número %d é par" % numero

    else:

        return "O número %d é impar" % numero


def calculo_fatorial (numero: int):

    resultado_fatorial = numero

    for contador in range(numero, 1, -1):

        resultado_fatorial *= contador - 1

    return f"{resultado_fatorial}"


def ano_bissexto (ano: int):

    if ano % 4 == 0:

        if ano % 100 != 0:

            return "O ano %d é bissexto" % ano

        elif ano % 100 == 0:

            return "O ano %d é bissexto especial" % ano

    else:

        return "O ano %d não é bissexto" % ano


def numero_decimal_inteiro (numero: float):

    import math

    numero_decimal = numero

    numero_inteiro = math.trunc(numero_decimal)

    if numero_decimal > numero_inteiro or numero_decimal != numero:

        return True

    else:

        numero_decimal = str(numero_decimal)

        if "." in numero_decimal:

            return True

        else:

            return False


def numero_fizz_buzz (numero_limite: int):

    if numero_limite <= 0:

        return "Número menores que 1 não são válidos"

    if numero_limite % 3 == 0 and numero_limite % 5 == 0 and numero_limite != 0:

        return "O número %d é FizzBuzz" % numero_limite

    elif numero_limite % 3 == 0:

        return "O número %d é Fizz" % numero_limite

    elif numero_limite % 5 == 0:

        return "O número %d é Buzz" % numero_limite

    else:

        return "O número %d não é nem Fizz nem Buzz" % numero_limite


def binary_decimal (numero: str):

    tamanho_decimal = len(numero)

    decimal = 0

    expoente = tamanho_decimal - 1

    for contador in numero:

        if contador == "1":

            decimal += (1 * 2 ** expoente)

        elif contador == "0":

            decimal += (0 * 2 ** expoente)

        else:

            return 'Esse não é um número binário'

        expoente -= 1

        numero = int(numero)

    return f"{decimal}"


def decimal_binary (numero: int):

    resto = []

    binario = ""

    numero_decimal = numero

    while numero_decimal != 0:

        resto.insert(0, numero_decimal % 2)

        numero_decimal = numero_decimal // 2

    for contador in resto:

        binario += str(contador)

    binario = int(binario)

    return f"{binario}"