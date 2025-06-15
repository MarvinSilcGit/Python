nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 7:

    print(f"O aluno foi reprovado com a nota {media:.2f}")

elif media < 10:

    print(f"O aluno foi aprovado com a nota {media:.2f}")

else:

    print(f"O aluno foi aprovado com distinção através da nota {media:.2f}")