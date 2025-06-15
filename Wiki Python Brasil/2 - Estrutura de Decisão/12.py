carga_horaria = int(input("Digite a sua carga horária mensal: "))

salario_hora = float(input("Digite o seu salário hora: "))

salario_bruto = carga_horaria * salario_hora

descontos = 0

imposto_renda = 0

inss = 0

if salario_bruto <=  900:

    print(f"O salário será R$ {salario_bruto:.2f}, com R$ {imposto_renda:.2f} de Imposto de renda, R$ {inss:.2f} de INSS. Totalizando R$ {descontos:.2f} em descontos")

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

print(f"O salário inicial era de R$ {salario_bruto:.2f} e será R$ {salario_bruto-descontos:.2f}, com R$ {imposto_renda:.2f} de Imposto de renda e R$ {inss:.2f} de INSS. Totalizando R$ {descontos:.2f} em descontos")