contador = 1

while contador != 0:

    dict_estado_civil = {"s": "Solteiro", "v": "Viúvo", "c": "Casado", "d": "Divorciado"}

    nome = input("Digite seu nome: ")

    if len(nome) < 3:

        print("Nome muito pequeno")

        continue


    while True:

        idade = int(input("Digite sua idade: "))

        if 0 <= idade < 150: # Equals to if idade >=0 and idade < 150:

            break

        else:

            print("Idade inválida")


    while True:

        salario = float(input("Digite o seu salário: "))

        if salario > 0:

            break

        else:

            print("Salário inválido")


    while True:

        sexo = input("Digite o seu sexo:\nf - mulheres\nm - homens\n")

        print(sexo)

        if sexo == "m" or sexo == "f":

            break


        else:

            print("Sexo inválido")


    while True:

        estado_civil = input("Digite seu estado civil:\ns - solteiro(a)\nv - viúvo(a)\nc - casado(a)\nd - divorciado\n")

        if estado_civil in dict_estado_civil:

            break

        else:

            print("Estado civil inválido")


    sexo = "Masculino" if sexo == "m" else "Feminino"

    print(f"{nome} {idade} anos, {salario:,.2f} de salário, sexo {sexo} e {dict_estado_civil.get(estado_civil)}")

    contador = int(input("Digite 0 para finalizar o programa: "))