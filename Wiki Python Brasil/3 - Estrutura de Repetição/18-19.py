contador = 1

maior_numero = 0

menor_numero = 0

while contador != 0:

    numero = int(input("Digite um número ou 0 para interromper a execução: "))

    if numero == 0:

        contador = 0

    else:

        if numero > 1000 or numero < 1:

            print("Valor inválido")

            continue

        else:

            if menor_numero == 0:

                menor_numero = numero

            if maior_numero < numero:

                maior_numero = numero

            if menor_numero > numero:

                menor_numero = numero

if maior_numero == menor_numero:

    print("Os números são idênticos")

else:

    print(f"O maior número foi {maior_numero} e o menor número foi {menor_numero}")