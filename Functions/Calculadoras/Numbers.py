from Functions.Calculadoras.Validations import numero_primo


def resto_divisao (valor1: float, valor2: float):

    resto = 0

    if valor1 == 0 or valor2 == 0:

        return "Divisão por zero inválida"

    else:

        if valor1 == valor2:

            return f"{resto}"

        elif valor1 > valor2:

            while valor2 + resto <= valor1:

                resto += valor2

            resto = valor1 - resto

        else:

            while valor1 + resto < valor2:

                resto += valor1

            while resto != valor2:

                resto += 1

        return f"{resto}"


def resto_inteiro_divisao (valor1: float, valor2: float):

    resto_inteiro = 0

    resto = 0

    if valor1 == 0 or valor2 == 0:

        return False

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

    resultado_raiz_quadrada **= 2

    while resultado_raiz_quadrada * resultado_raiz_quadrada - numero > 0.001:

        base = resultado_raiz_quadrada

        resultado_raiz_quadrada = (base + numero / base) / 2

    return f"{resultado_raiz_quadrada:,.4f}"


def calculo_fatorial (numero: int):

    resultado_fatorial = numero

    for contador in range(numero, 1, -1):

        resultado_fatorial *= contador - 1

    return f"{resultado_fatorial}"


#print(equacao_segundo_grau_bhaskara(3,-6, -8))

def calculo_porcentagem_representante (valor1: float, valor2: float):

    porcentagem = (valor1 / valor2) * 100

    return f'{valor1:,.2f} representa {porcentagem:,.2f}% de {valor2:,.2f}'


def minimo_multiplo_comum (valor1: float, valor2: float):

    numero_primo_inicial = 2

    mmc = []

    while valor1 != 1.0:

        if valor1 % numero_primo_inicial == 0:

            valor1 /= numero_primo_inicial

            mmc.append(numero_primo_inicial)

        if valor2 % numero_primo_inicial == 0:

            valor2 /= numero_primo_inicial

            if numero_primo_inicial not in mmc:

                mmc.append(numero_primo_inicial)

        else:

            numero_primo_inicial += 1

    return mmc

print(minimo_multiplo_comum(10, 7))