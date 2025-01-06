carga_horaria = int(input("Digite a sua carga horária mensal: "))

salario_hora = float(input("Digite o seu salário hora: "))

salario_bruto = carga_horaria * salario_hora

descontos = 0

imposto_renda = 0

inss = 0

if salario_bruto <=  900:

    print("O salário será R$ %.2f com R$ %.2f de Imposto de renda, R$ %.2f de INSS. Totalizando R$ %.2f em descontos" % (salario_bruto, imposto_renda, inss, descontos))

elif salario_bruto <= 1500:

    imposto_renda = salario_bruto / 100 * 5

    inss = salario_bruto / 100 * 10

    descontos = imposto_renda + inss

elif salario_bruto <= 2500:

    imposto_renda = salario_bruto / 100 * 10

    inss = salario_bruto / 100 * 10

    descontos = imposto_renda + inss

elif salario_bruto > 2500:

    imposto_renda = salario_bruto / 100 * 20

    inss = salario_bruto / 100 * 10

    descontos = imposto_renda + inss

print("O salário inicial era de R$ %.2f e será R$ %.2f, com R$ %.2f de Imposto de renda e R$ %.2f de INSS. Totalizando R$ %.2f em descontos" % (salario_bruto, salario_bruto - descontos, imposto_renda, inss, descontos))