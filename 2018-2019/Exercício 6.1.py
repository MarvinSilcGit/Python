notas = [0, 0, 0, 0, 0, 0, 0]

soma = 0

n = 0

cont = 1

alunos = ["Marcos", "Pedro", "Ana"]

cont2 = 0

while cont != 0:

    while n < 7:

        notas[n] = float(input("digite a %d° nota  do aluno(a) %s: " % (n+1, alunos[cont2])))

        soma += notas[n]

        n += 1

    n = 0

    while n < 7:

        n += 1

    print("A média do(a) aluno(a) %s é : %0.2f " % (alunos[cont2], soma/n))

    cont = int(input("digite 0 para interromper: "))

    if cont != 0:

        n = 0

        soma = 0

        nota = [0, 0, 0, 0, 0, 0, 0]

        cont2 += 1
