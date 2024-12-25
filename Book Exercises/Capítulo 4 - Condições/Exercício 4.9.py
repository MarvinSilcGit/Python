valorCasa = float(input("Qual o valor da casa? "))

salario = float(input("Qual o seu salário? "))

anos = int(input("Irá pagar em quantos anos? "))

anos *= 12

parcelasMensais = valorCasa / anos

porcentagem = salario / 100 * 30

if valorCasa / anos  < porcentagem:

    print("O usuário poderá contratar o financiamento, pois parcela não é superior a um terço de sua renda mensal. As parcelas serão de R$ %.2f" % parcelasMensais)

else:

    print("O usuário não poderá contratar o financiamento, pois parcela é superior a um terço de sua renda mensal. As parcelas seriam de R$ %.2f" % parcelasMensais)