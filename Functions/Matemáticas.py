#How to import: from Functions.Matemáticas import resto_divisao or import *


def resto_divisao (valor1, valor2):

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


def resto_inteiro_divisao (valor1, valor2):

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

        return "O resto inteiro da divisão entre %.1f e %.1f é: %d" % (valor1, valor2, resto_inteiro)


def raiz_quadrada (numero):

    base = 2

    resultado_raiz_quadrada = (base + numero / base) / 2

    resultado_raiz_quadrada = resultado_raiz_quadrada ** 2

    while resultado_raiz_quadrada * resultado_raiz_quadrada - numero > 0.001:

        base = resultado_raiz_quadrada

        resultado_raiz_quadrada = (base + numero / base) / 2

    return "A raiz aproximada de %d é: %.4f" % (numero, resultado_raiz_quadrada)


def numero_primo (numero):

    confirmacao = 2

    if numero == 0 or numero == 1:

        return "Esse número é inválido"

    if numero ==  2 or numero == 3:

        return "%d é um número primo" % numero

    else:

        for contador2 in range(2, numero + 1):

            if numero % contador2 != 0:

                confirmacao += 1

        if confirmacao == numero:

            return "%d é um número primo" % numero

        else:

            return"%d não é um número primo" % numero


def numero_par (numero):

    if numero % 2 == 0:

        return "O número %d é par" % numero


def numero_impar (numero):

    if numero % 2 !=0:

        return "O número %d é ímpar" % numero


def valor_palindromo (valor):

    contador2 = 0

    if len(valor) < 2:

        return "Tamanho insuficiente!"

    else:

        for contador1 in range(0, len(valor)):

            if valor[0 + contador1] == valor[-1 - contador1]:

                contador2 += 1

        if contador2 == len(valor):

            return "%s é palíndromo" % valor

        else:

            return "%s não é palíndromo" % valor

def atm_machine (valor):

    valor = valor

    cedula200 = 0

    cedula100 = 0

    cedula50 = 0

    cedula20 = 0

    cedula10 = 0

    cedula5 = 0

    cedula2 = 0

    valor_saque = valor

    moeda50 = 0
    moeda25 = 0
    moeda10 = 0
    moeda5 = 0

    while True:

        if valor < 2:

            return "R$ %.2f é um valor inválido para saque" % valor_saque

        else:

            return 0

print(atm_machine(3))