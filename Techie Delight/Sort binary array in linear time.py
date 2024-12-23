# Source https://www.techiedelight.com/sort-binary-array-linear-time/

import random

Array, Exchange, Counter1 = [], [], 0

for Counter in range(0, random.randint(5, 30)):

    Array.append(random.randrange(0, 2))

print("The original Array is: ", Array)

while Counter1 != len(Array)-1:

    if Array[Counter1] > 0:

        Exchange.append(Array.pop(Counter1))

        Counter1 = 0

    else:

        Counter1 += 1

        continue

while True:

    Array.append(Exchange.pop(0))

    if len(Exchange) == 0:

        break

print("The new Array sorted in Binary: ", Array)
