contador = 1

maiorNumero = 0

menorNumero = 0

while contador != 0:

    numero = int(input("Digite um número ou 0 para interromper a execução: "))

    if numero == 0:

        contador = 0

    else:

        if numero > 1000:

            print("Valor inválido")

            continue

        else:

            if numero > maiorNumero:

                maiorNumero = numero

                menorNumero = numero

            if numero < menorNumero:

                menorNumero = numero

if maiorNumero == menorNumero:

    print("O número são idênticos")

else:

    print("O maior número foi %d e o menor número foi %d" % (maiorNumero, menorNumero))