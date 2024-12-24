nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 7:

    print("O aluno foi reprovado com a nota %.2f" % media)

elif media < 10:

    print("O aluno foi aprovado com a nota %.2f" % media)

else:

    print("O aluno foi aprovado com distinção através da nota %.2f" % media)