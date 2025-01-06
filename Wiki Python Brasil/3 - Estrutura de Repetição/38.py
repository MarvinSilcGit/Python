salario = float(input("Digite o salário inicial: "))

juros_inicial = 1.5

for contador in range(1996, 2024 + 1):

    salario += salario / 100 * juros_inicial

    juros_inicial = juros_inicial * 2

    print("R$ %.2f de salário no ano de %d" % (salario, contador))