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


def atm_machine (valor_pagamento):

    valor_pagamento = valor_pagamento

    if valor_pagamento < 1:

        return "Valor insuficiente para saque"

    else:

        cedulas = 0

        limite_cedula = 200

        limite_moeda = 0.5

        valor_retirada = valor_pagamento

        moeda = 0

        resultado = []

        while True:

            if limite_cedula <= valor_retirada:

                valor_retirada -= limite_cedula

                cedulas += 1

            else:

                resultado.append("%d cédula(s) de R$ %.2f" % (cedulas, limite_cedula))

                if valor_retirada == 0:

                    return resultado

                if limite_cedula == 200:

                    limite_cedula = 100

                elif limite_cedula == 100:

                    limite_cedula = 50

                elif limite_cedula == 50:

                    limite_cedula = 20

                elif limite_cedula == 20:

                    limite_cedula = 10

                elif limite_cedula == 10:

                    limite_cedula = 5

                elif limite_cedula == 5:

                    limite_cedula = 1

                cedulas = 0

                """elif limite_moeda == 1:
    
                    limite_moeda = 0.5
    
                elif limite_moeda == 0.50:
        
                    limite_moeda = 0.10
        
                elif limite_moeda == 0.10:
        
                    limite_moeda = 0.05

                elif limite_moeda == 0.05:
        
                    limite_moeda = 0.02

                elif limite_moeda == 0.02:
        
                    limite_moeda = 0.01"""

"""Acessar Valores
for contador2 in range(0, 10):

    for contador in atm_machine(contador2):

        print(contador)

print(atm_machine(0))"""