mons = [-10, -8, 0, 1, 2, 5, -2, -4]

maxi = mons[0]

media = 0

tot = 0

for e in mons:

    media += e

    tot += 1

    if e > maxi:

        maxi = e

print("A temperatura máxima foi de: %d°" % maxi)

mini = mons[0]

for d in mons:

    if d < mini:

        mini = d

print("A temperatura mínima foi de: %d°" % mini)

print()

media = media/tot

print("A temperatura média foi de: %.2f°" % media)
