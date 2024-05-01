ult = 10

fila = list(range(1, 10 + 1))

fila2 = fila[:]

ult1 = ult

while True:

    print("Existem %d clientes na primeira fila e %d clientes na segunda fila" % (len(fila), len(fila2)))

    print("**********************************************")

    fil = int(input("Digite 1 para acessar a fila 1;  2 para a fila 2; ou 0 para interromper a execução: "))

    if fil == 1:

        print("**********************************************")

        print("Fila 1:", fila)

        print("Digite f para adicionar um cliente ao fim da fila primeira, ")

        print("a para realizar o atendimento na primeira fila e s para sair")

        op = list(input("Operação: "))

        x = 0

        print("**********************************************")

        while x != len(op):

            if (op[x]) == "a":

                if (len(fila)) > 0:

                    ate = fila.pop(0)

                    print("Cliente %d da primeira atendido" % ate)

                elif (len(fila)) <= 0:

                    print("Fila vazia! Ninguém para atender")

            elif (op[x]) == "f":

                ult += 1

                fila.append(ult)

                print("Cliente %d entrou na fila" % ult)

            elif (op[x]) != "a" and (op[x]) != "f" and (op[x]) != "s":

                print("Operação inválida! Digite corretamente")

                break

            if len(op) == 1:

                break

            elif len(op) > 1:

                x += 1

        print("**********************************************")

    elif fil == 2:

        print("#######################################")

        print("Fila 2: ", fila2)

        print("Digite f para adicionar um cliente ao fim da segunda fila, ")

        print("a para realizar o atendimento na segunda fila e s para sair")

        op = list(input("Operação: "))

        x = 0

        print("#######################################")

        while x != len(op):

            if (op[x]) == "a":

                if (len(fila2)) > 0:

                    eta = fila2.pop(0)

                    print("Cliente %d da segunda fila atendido" % eta)

                elif (len(fila2)) <= 0:

                    print("Fila vazia! Niguém para atender")

            elif (op[x]) == "f":

                ult1 += 1

                fila2.append(ult1)

                print("Cliente %d entrou na fila" % ult1)

            elif (op[x]) != "a" and (op[x]) != "f" and (op[x]) != "s":

                print("Operação inválida! Digite corretamente")

                break

            if len(op) == 1:

                break

            elif len(op) > 1:

                x += 1

    elif (fil != 0) and (fil != 1) and (fil != 2):

        print("Digite os valores corretamente")

        break

    elif fil == 0:

        break
