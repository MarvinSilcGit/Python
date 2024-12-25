casaValor = float(input("Qual o valor da casa? "))

salario = float(input("Qual o seu salário? "))

anos = int(input("Irá pagar em quantos anos? "))

anos = anos * 12

parcelas = casaValor / anos

porcentagem = salario * 0.3

if parcelas > porcentagem:

    print("O usuário em questão não está apto para realizar um financiamento, pois possui um renda que não é 70% superior ao valor do financiamento")

elif parcelas <= porcentagem:

    print("O usuário em questão está apto para aderir a um financiamento, pois possui uma renda 70% superior ao valor do financiamento")
