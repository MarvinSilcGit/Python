# Source: https://www.techiedelight.com/find-pair-with-given-sum-array/

import random

Counter1, Counter2, Array, RandomLen, par = 0, 0, [], [], []

Goal = random.randint(1, 30)

for Counter in range(15):

    RandomLen.append(random.randint(1, 15))

    if RandomLen[Counter] in Array:

        continue

    else:

        Array.append(RandomLen[Counter])

while Counter1 != len(Array):

    if Array[Counter1] == Array[Counter2]:

        Counter1 += 1

        continue

    elif Array[Counter1] + Array[Counter2] == Goal or Array[Counter1] - Array[Counter2] == Goal:

        if Array[Counter2] and Array[Counter1] not in par:

            par.append(Array[Counter1])

            par.append(Array[Counter2])

        else:

            pass

    if Counter1 == len(Array)-1:

        Counter2 += 1

        Counter1 = 0

        continue

    else:

        Counter1 += 1

print("The Bullseye-Array", Array)

print()

print("The Goal is", Goal)

print()

if len(par) > 1:

    print("The pairs that matchs:", par)

elif len(par) == 1:

    print("The only one pair that matchs:", par)
