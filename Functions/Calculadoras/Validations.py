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


def ano_bissexto (ano: int):

    if ano % 4 == 0:

        if ano % 100 != 0:

            return "O ano %d é bissexto" % ano

        elif ano % 100 == 0:

            return "O ano %d é bissexto especial" % ano

    else:

        return "O ano %d não é bissexto" % ano


def validade_numero_decimal (numero: float):

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
