def desenhar_quadrado (lado_quadrado: float):

    lado_quadrado = int(lado_quadrado)

    for _ in range(lado_quadrado):

        print("*  " * lado_quadrado)

    return ''
print(desenhar_quadrado(8))