# Source: https://www.techiedelight.com/find-pair-with-given-sum-array/

import random

# Fix this code. It should only find a pair with sum, not sum and sub

counter1, counter2, array, randomLen, par = 0, 0, [], [], []

goal = random.randint(1, 30)

for Counter in range(15):

    randomLen.append(random.randint(1, 15))

    if randomLen[Counter] in array:

        continue

    else:

        array.append(randomLen[Counter])

while counter1 != len(array):

    if array[counter1] == array[counter2]:

        counter1 += 1

        continue

    elif array[counter1] + array[counter2] == goal or array[counter1] - array[counter2] == goal:

        if array[counter2] and array[counter1] not in par:

            par.append(array[counter1])

            par.append(array[counter2])

        else:

            pass

    if counter1 == len(array)-1:

        counter2 += 1

        counter1 = 0

        continue

    else:

        counter1 += 1

print("The Bullseye-Array", array)

print()

print("The Goal is", goal)

print()

if len(par) > 1:

    print("The pairs that matchs:", par)

elif len(par) == 1:

    print("The only one pair that matchs:", par)
