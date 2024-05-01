L = [7, 4, 3, 12, 8]

fim = 5

while fim > 1:

    trocou = False

    x = 0

    while x < (fim-1):

        if L[x] < L[x+1]:

            trocou = True

            temp = L[x+1]

            L[x+1] = L[x]

            L[x] = temp

        x += 1

    if not trocou:

        break

    fim -= 1

for e in L:

    print(e)
