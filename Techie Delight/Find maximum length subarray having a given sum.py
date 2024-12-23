# Source https://www.techiedelight.com/find-maximum-length-sub-array-having-given-sum/

import random

Counter1, Counter2, Sum, Array, RandomLen, SubArray = 0, 1, 0, [], [], []

Goal = random.randint(1, 30)

for Counter in range(15):

    RandomLen.append(random.randint(1, 15))

    if RandomLen[Counter] in Array:

        continue

    else:

        Array.append(RandomLen[Counter])

Sum = Array[Counter1]

SubArray.append(Array[Counter1])

while Counter1 != len(Array) - 1:

    if Sum + Array[Counter2] <= Goal:

        SubArray.append(Array[Counter2])

        Sum += Array[Counter2]

# if Sum != Goal and Array[Counter2 + 1] + Sum > Goal:

# Sum -= Array[Counter2]

    Counter2 += 1

    if Counter2 == len(Array):

        Counter1 += 1

        Counter2 = Counter1 + 1

        print(SubArray)

        Sum = Array[Counter1]

        SubArray.append("|")

        if Array[Counter1] <= Goal:

            SubArray.append(Array[Counter1])

print()
print(Array)
print(Goal)
print(SubArray)

# 24
# 2, 6, 10, 9, 11, 15, 12, 13
