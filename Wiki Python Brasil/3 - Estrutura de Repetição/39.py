contador = 1

numero = 0

maior_altura = 0

menor_altura = 0

numero_aluno_baixo = 0

numero_aluno_alto = 0

while contador != 0:

    altura = float(input("Digite a altura do aluno: "))

    numero = int(input("Digite o número do aluno: "))

    if altura < 0.5 or numero < 1:

        print("Valores incorretos")

        continue

    else:

        if menor_altura == 0:

            menor_altura = altura

            numero_aluno_baixo = numero

        if maior_altura < altura:

            maior_altura = altura

            numero_aluno_alto = numero

        if menor_altura > altura:

            menor_altura = altura

            numero_aluno_baixo = numero

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()

print("O aluno com o número %d teve a maior altura %.2f" % (numero_aluno_alto, maior_altura))

print("O aluno com o número %d teve a menor altura %.2f" % (numero_aluno_baixo, menor_altura))