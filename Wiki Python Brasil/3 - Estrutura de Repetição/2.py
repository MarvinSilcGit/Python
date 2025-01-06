contador = 1

while contador != 0:

    nome = input("Digite o nome de usuário: ")

    senha = input("Digite a senha: ")

    if nome == senha:

        print("Usuário e senha não podem ser idênticos")

        continue

    contador = int(input("Digite 0 para finalizar o programa: "))