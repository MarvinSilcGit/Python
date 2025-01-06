contador = 1

maiorNumero = 0

menorNumero = 0

while contador != 0:

    numero = int(input("Digite um número ou 0 para interromper a execução: "))

    if numero == 0:

        contador = 0

    else:

        if numero > 1000 or numero < 1:

            print("Valor inválido")

            continue

        else:

            if menorNumero == 0:

                menorNumero = numero

            if maiorNumero < numero:

                maiorNumero = numero

            if menorNumero > numero:

                menorNumero = numero

if maiorNumero == menorNumero:

    print("Os números são idênticos")

else:

    print("O maior número foi %d e o menor número foi %d" % (maiorNumero, menorNumero))