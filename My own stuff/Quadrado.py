lado_quadrado = input("Digite o tamanho de um lado do quadrado: ")

if lado_quadrado.isdigit():

    lado_quadrado = int(lado_quadrado)

    for _ in range(lado_quadrado):

        print("*  " * lado_quadrado)