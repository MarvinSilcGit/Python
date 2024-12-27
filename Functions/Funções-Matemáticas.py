def divisao_resto (valor1, valor2):

    resto_inteiro = 0

    resto = 0

    if valor1 == 0 or valor2 == 0:

        return "Divisão por zero inválida"

    else:

        if valor1 == valor2:

            resto_inteiro = 1

        elif valor1 > valor2:

            while valor2 + resto < valor1:

                resto_inteiro += 1

                resto += valor2

            resto = valor1 - resto

        else:

            while valor1 + resto < valor2:

                resto += valor1

            while resto != valor2:

                resto += 1

        return "O resto da divisão entre %.1f e %.1f é: %.1f" % (valor1, valor2, resto)

def divisao_inteira_resto (valor1, valor2):

    resto_inteiro = 0

    resto = 0

    if valor1 == 0 or valor2 == 0:

        return "Divisão por zero inválida"

    else:

        if valor1 == valor2:

            resto_inteiro = 1

        elif valor1 > valor2:

            while valor2 + resto < valor1:

                resto_inteiro += 1

                resto += valor2

            resto = valor1 - resto

        else:

            while valor1 + resto < valor2:

                resto += valor1

            while resto != valor2:

                resto += 1

        return "O resto inteiro da divisão entre %.1f e %.1f é: %d. E o resto da divisão é %.1f" % (valor1, valor2,resto_inteiro, resto)

def raiz_quadrada (valor):

    base = 2

    resultado_raiz_quadrada = (base + valor / base) / 2

    resultado_raiz_quadrada = resultado_raiz_quadrada ** 2

    while resultado_raiz_quadrada * resultado_raiz_quadrada - valor > 0.001:

        base = resultado_raiz_quadrada

        resultado_raiz_quadrada = (base + valor / base) / 2

    return "A raiz aproximada de %d é: %.4f" % (valor, resultado_raiz_quadrada)

print(raiz_quadrada(5))