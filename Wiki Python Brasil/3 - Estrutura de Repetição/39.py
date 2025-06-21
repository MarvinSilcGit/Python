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

print(f"O aluno com o número {numero_aluno_alto} teve a maior altura {maior_altura:.2f}")

print(f"O aluno com o número {numero_aluno_baixo} teve a menor altura {menor_altura:.2f}")