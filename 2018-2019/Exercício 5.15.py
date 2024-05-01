cont1 = 1

cont = 0

total = 0

while cont1 != 0:

    vcod = 1

    while vcod != 0:

        print()

        print("Se não deseja nenhum produto digite o valor 0")

        print()

        print("código 1, referente ao produto A; com valor de R$ 0,50")

        print()

        print("código 2, referente ao produto B; com valor de R$ 1,00")

        print()

        print("código 3, referente ao produto C; com valor de R$ 4,00")

        print()

        print("código 5, referente ao produto E, com valor de R$ 7,00")

        print()

        print("código 9, referente ao produto I; com valor de R$ 8,00")

        print()

        vcod = float(input("Digite o código do produto desejado: "))

        if vcod == 0:

            print()

            print("O valor total das compras foi de R$ %.2f"%total)

            break

        elif vcod == 1:

            vqua = int(input("Digite a quantidade desejada do produto A: "))

            vqua = vqua*0.5

            total += vqua

        elif vcod == 2:

            vqua = int(input("Digite a quantidade desejada do produto B: "))

            vqua = vqua*1

            total += vqua

        elif vcod == 3:

            vqua = int(input("Digite a quantidade desejada do produto C: "))

            vqua = vqua*4

            total += vqua

        elif vcod == 5:

            vqua = int(input("Digite a quantidade desejada do produto E: "))

            vqua = vqua*7

            total += vqua

        elif vcod == 9:

            vqua = int(input("Digite a quantidade desejada do produto I: "))

            vqua = vqua*8

            total += vqua

        elif vcod != 0 or vcod != 1 or vcod != 2 or vcod != 3 or vcod != 5 or vcod != 9:

            print("Valor incorreto digitado")

            break

        print("O valor atual das compras é de %2.2f R$:" % total)

    print()

    cont1 = int(input("Digite 0 para interromper a execução: "))
