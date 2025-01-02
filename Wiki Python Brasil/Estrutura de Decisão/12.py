cargaHoraria = int(input("Digite a sua carga horária mensal: "))

salarioHora = float(input("Digite o seu salário hora: "))

salarioBruto = cargaHoraria * salarioHora

descontos = 0

impostoRenda = 0

inss = 0

if salarioBruto <=  900:

    print("O salário será R$ %.2f com R$ %.2f de Imposto de renda, R$ %.2f de INSS. Totalizando R$ %.2f em descontos" % (salarioBruto, impostoRenda, inss, descontos))

elif salarioBruto <= 1500:

    impostoRenda = salarioBruto / 100 * 5

    inss = salarioBruto / 100 * 10

    descontos = impostoRenda + inss

elif salarioBruto <= 2500:

    impostoRenda = salarioBruto / 100 * 10

    inss = salarioBruto / 100 * 10

    descontos = impostoRenda + inss

elif salarioBruto > 2500:

    impostoRenda = salarioBruto / 100 * 20

    inss = salarioBruto / 100 * 10

    descontos = impostoRenda + inss

print("O salário inicial era de R$ %.2f e será R$ %.2f, com R$ %.2f de Imposto de renda e R$ %.2f de INSS. Totalizando R$ %.2f em descontos" % (salarioBruto, salarioBruto-descontos, impostoRenda, inss, descontos))