# Source https://www.techiedelight.com/sort-binary-array-linear-time/

import random

array, exchange, counter1 = [], [], 0

for counter in range(0, random.randint(5, 30)):

    array.append(random.randrange(0, 2))

print("The original Array is: ", array)

while counter1 != len(array)-1:

    if array[counter1] > 0:

        exchange.append(array.pop(counter1))

        counter1 = 0

    else:

        counter1 += 1

        continue

while True:

    array.append(exchange.pop(0))

    if len(exchange) == 0:

        break

print("The new Array sorted in Binary: ", array)
