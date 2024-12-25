numero1 = float(input("Digite o primeiro valor: "))

print("Digite 1 para somar")

print("Digite 2 para subtrair")

print("Digite 3 para multiplicar")

print("Digite 4 para dividir")

print()

operadores = input("Qual operador deseja utilizar na operação? ")

print()

numero2 = float(input("Digite o segundo valor: "))

print()

if operadores == "1":

    soma = numero1 + numero2

    print("O resultado da soma entre %.1f e %.1f é %.1f" % (numero1, numero2, soma))

elif operadores == "2":

    soma = numero1 - numero2

    print("O resultado da subtração entre %.1f e %.1f é %.1f" % (numero1, numero2, soma))

elif operadores == "3":

    soma = numero1 * numero2

    print("O resultado da multiplicação entre %.1f e %.1f é %.1f" % (numero1, numero2, soma))

elif operadores == "4":

    soma = numero1 / numero2

    print("O resultado da divisão entre %.1f e %.1f é %.1f" % (numero1, numero2, soma))

elif operadores != 1 and operadores != 2 and operadores != 3 and operadores != 4:

    print("Digite um número entre 1 e 4 para concluir a operação")