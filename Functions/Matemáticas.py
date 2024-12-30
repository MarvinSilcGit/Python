#How to import: from Functions.Matemáticas import resto_divisao or import *


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

        return "O resto inteiro da divisão entre %.1f e %.1f é: %d" % (valor1, valor2, resto_inteiro)


def raiz_quadrada (numero: float):

    base = 2

    resultado_raiz_quadrada = (base + numero / base) / 2

    resultado_raiz_quadrada = resultado_raiz_quadrada ** 2

    while resultado_raiz_quadrada * resultado_raiz_quadrada - numero > 0.001:

        base = resultado_raiz_quadrada

        resultado_raiz_quadrada = (base + numero / base) / 2

    return "A raiz aproximada de %d é: %.4f" % (numero, resultado_raiz_quadrada)


def numero_primo (numero: int):

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


def numero_par (numero: int):

    if numero % 2 == 0:

        return "O número %d é par" % numero


def numero_impar (numero: int):

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


def atm_machine (valor: float):

    valor_pagamento = valor

    if valor_pagamento < 1:

        return "Valor insuficiente para saque"

    else:

        cedulas = 0

        limite_cedula = 200

        resultado = []

        limite_moeda = 0.5

        moedas = 0

        while True:

            if limite_cedula <= valor_pagamento:

                valor_pagamento -= limite_cedula

                cedulas += 1

            else:

                resultado.append("%d cédula(s) de R$ %.2f" % (cedulas, limite_cedula))

                if valor_pagamento == 0:

                    return resultado

                else:

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

                        limite_cedula = 2

                    elif limite_cedula == 2:

                        limite_cedula = 1

                    cedulas = 0

                    if 0 < valor_pagamento < 1:

                        if limite_moeda <= valor_pagamento:

                            valor_pagamento -= limite_moeda

                            moedas += 1

                            if valor_pagamento == 0:

                                resultado.append("%d moeda(s) de R$ %.2f" % (moedas, limite_moeda))

                                return resultado

#Acessar Valores
"""for contador2 in range(1, 100):

    for contador in atm_machine(contador2):

        print(contador)

print(atm_machine(11.5))"""


def calculo_fatorial (numero: int):

    numero = numero

    resultado_fatorial = numero

    for contador in range(numero, 1, -1):

        resultado_fatorial *= contador - 1

    return "Fatorial de %d é %d" % (numero, resultado_fatorial)


def raio_circulo (area: float):

    area_circulo = 3.14 * (area ** 2)

    return area_circulo


def fahrenheit_celsius (temperatura: float):

    fahrenheit = temperatura

    celsius = (fahrenheit - 32) / 1.8

    return "A temperatura em %.1f° fahrenheit equivale à %.1f° celsius" % (fahrenheit, celsius)


def celsius_fahrenheit (temperatura: float):

    celsius = temperatura

    fahrenheit = (celsius * 1.8) + 32

    return "A temperatura em %.1f° celsius equivale à %.1f° fahrenheit" % (celsius, fahrenheit)


def calculo_imc (peso: float, altura: float):

    indice_massa_corporea = peso / altura ** 2

    return indice_massa_corporea


def calculo_tbm (peso: float, altura: float, idade: int, genero: str):

    lista_generos = ["Masculino", "masculino", "Feminino", "feminino"]

    if genero not in lista_generos:

        return "Genêro inválido"

    else:

        peso = peso

        altura = altura

        idade = idade

        genero = genero

        if genero == "Masculino" or genero == "masculino":

            taxa_basal_metabolica = 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)

            return taxa_basal_metabolica

        elif genero == "Feminino" or genero == " feminino":

            taxa_basal_metabolica = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)

            return taxa_basal_metabolica