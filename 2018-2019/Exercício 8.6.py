def soma(L):

    total = 0
    x = 0

    while x<5:

		total += L[x]
		x += 1

    return total

L=[1,7,2,9,15]

print(soma(L))

print(soma([7,9,12,3,100,20,4]))