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

    cedula200, cedula100, cedula50, cedula20, cedula10, cedula5, cedula2 = 0, 0, 0, 0, 0, 0, 0

    moeda50, moeda25, moeda10, moeda5 = 0, 0, 0, 0

    valor_saque = 0

    while valor_saque!= valor:

        if valor < 2 or valor == 3:

            return "R$ %.2f é um valor inválido para saque" % valor

        else:

            if cedula200 + 1 * 200 + valor_saque <= valor:

                cedula200 += 1

                valor_saque += 200

            elif cedula100 + 1 * 100 + valor_saque <= valor:

                cedula100 += 1

                valor_saque += 100

            elif cedula50 + 1 * 50 + valor_saque <= valor:

                cedula50 += 1

                valor_saque += 50

            elif cedula20 + 1 * 20 + valor_saque <= valor:

                cedula20 += 1

                valor_saque += 20

            elif cedula10 + 1 * 10 + valor_saque <= valor:

                cedula10 += 1

                valor_saque += 10

            elif cedula5 + 1 * 5 + valor_saque <= valor:

                cedula5 += 1

                valor_saque += 5

            elif cedula2 + 1 * 2 + valor_saque <= valor:

                cedula2 += 1

                valor_saque += 2

    return "Foram utilizadas %d cédula(s) de 200, %d cédula(s) de 100, %d cédula(s) de 50, %d cédula(s) de 20, %d cédula(s) 10, %d cédula(s) de 5 e %d cédula(s) 2" % (cedula200, cedula100, cedula50, cedula20, cedula10, cedula5, cedula2)

print(atm_machine(250))