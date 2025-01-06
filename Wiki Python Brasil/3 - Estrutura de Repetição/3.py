contador = 1

while contador != 0:

    nome = input("Digite seu nome: ")

    if len(nome) < 3:

        print("Nome muito pequeno")

        continue

    else:

        idade = int(input("Digite sua idade: "))

        if idade < 0 or idade > 150:

            print("Idade inválida")

            continue

        else:

            salario = float(input("Digite o seu salário: "))

            if salario <= 0:

                print("Salário inválido")

                continue

            else:

                sexo = input("Digite o seu sexo:\nf - mulheres\nm - homens\n")

                print(sexo)

                if sexo != "m" and sexo != "f":

                    print("Sexo inválido")

                    continue

                else:

                    estado_civil = input("Digite seu estado civil:\ns - solteiro(a)\nv - viúvo(a)\nc - casado(a)\nd - divorciado\n")

                    if estado_civil != "s" and estado_civil != "v" and estado_civil != "c" and estado_civil != "d":

                        print("Estado civil inválido")

                        continue

                    else:

                        print("%s, %d, %.2f, %s, %s" % (nome, idade, salario, sexo, estado_civil))

    contador = int(input("Digite 0 para finalizar o programa: "))