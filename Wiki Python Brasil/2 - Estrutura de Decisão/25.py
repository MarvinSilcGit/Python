pergunta1 = input("Você telefonou para a vítima?: ")

pergunta2 = input("Você esteve no local do crime? ")

pergunta3 = input("Você mora perto da Vítima? ")

pergunta4 = input("Você devia para a vítima? ")

pergunta5 = input("Você já trabalhou com a vítima? ")

criminalidade = 0

list_possivel_resposta = ['Sim', 'sim']

if pergunta1 in list_possivel_resposta:

    criminalidade += 1

if pergunta2 in list_possivel_resposta:

    criminalidade += 1

if pergunta3 in list_possivel_resposta:

    criminalidade += 1

if pergunta4 in list_possivel_resposta:

    criminalidade += 1

if pergunta5 in list_possivel_resposta:

    criminalidade += 1

if criminalidade <= 1:

    print("Inocente")

elif criminalidade == 2:

    print("Suspeito")

elif criminalidade <= 4:

    print("Cúmplice")

elif criminalidade == 5:

    print("Assasino")