def numero_primo (numero: int):

    confirmacao = 2

    if numero == 0 or numero == 1:

        return False

    if numero ==  2 or numero == 3:

        return True

    else:

        for contador in range(confirmacao, numero + 1):

            if numero % contador != 0:

                confirmacao += 1

        if confirmacao == numero:

            return True

        else:

            return False


def numero_par_impar (numero: int):

    return numero % 2 == 0


def ano_bissexto (ano: int):

    if ano % 4 == 0:

        if ano % 100 != 0:

            return f"O ano {ano:d} é bissexto"

        else:

            return f"O ano {ano:d} é bissexto especial"

    else:

        return f"O ano {ano:d} não é bissexto"


def validade_numero_decimal (numero: float):

    import math

    numero_inteiro = math.trunc(numero)

    if numero_inteiro > numero or numero_inteiro != numero:

        return True

    else:

        numero_decimal = str(numero)

        if "." in numero_decimal:

            return True

        else:

            return False


def numero_fizz_buzz (numero_limite: int):

    if numero_limite <= 0:

        return "Número menores que 1 não são válidos"

    if numero_limite % 3 == 0 and numero_limite % 5 == 0 and numero_limite != 0:

        return f"O número {numero_limite:d} é FizzBuzz"

    elif numero_limite % 3 == 0:

        return f"O número {numero_limite:d} é Fizz"

    elif numero_limite % 5 == 0:

        return f"O número {numero_limite:d} é Buzz"

    else:

        return f"O número {numero_limite:d} não é nem Fizz nem Buzz"


def triangulo_tipo (lado1: int, lado2: int, lado3: int):

    if lado1 == 0 or lado2 == 0 or lado3 == 0:

        return "Um triângulo não pode ter lado 0"

    else:

        if lado1 + lado2 <= lado3:

            return "A soma desses lados não forma um triângulo"

        else:

            if lado1 == lado2 == lado3:

                return "Esse é um triângulo equilátero"

            elif lado1 != lado2 != lado3 != lado1:

                return "Esse é um triângulo escaleno"

            elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:

                return "Esse é um triângulo isosceles"


def palindromo (valor):

    contador2 = 0

    if len(valor) <= 2:

        return "Tamanho insuficiente!"

    else:

        for contador1 in range(0, len(valor)):

            if valor[contador1] == valor[- 1 - contador1]:

                contador2 += 1

        if contador2 == len(valor):

            return f"{valor:s} é palíndromo"

        else:

            return f"{valor:s} não é palíndromo"