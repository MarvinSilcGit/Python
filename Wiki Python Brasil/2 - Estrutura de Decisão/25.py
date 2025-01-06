pergunta1 = input("Você telefonou para a vítima?: ")

pergunta2 = input("Você esteve no local do crime? ")

pergunta3 = input("Você mora perto da Vítima? ")

pergunta4 = input("Você devia para a vítima? ")

pergunta5 = input("Você já trabalhou com a vítima? ")

criminalidade = 0

if pergunta1 == "Sim" or pergunta1 == "sim":

    criminalidade += 1

if pergunta2 == "Sim" or pergunta2 == "sim":

    criminalidade += 1

if pergunta3 == "Sim" or pergunta3 == "sim":
    criminalidade += 1

if pergunta4 == "Sim" or pergunta4 == "sim":

    criminalidade += 1

if pergunta5 == "Sim" or pergunta5 == "sim":

    criminalidade += 1

if criminalidade <= 1:

    print("Inocente")

elif criminalidade == 2:

    print("Suspeito")

elif criminalidade <= 4:

    print("Cúmplice")

elif criminalidade == 5:

    print("Assasino")