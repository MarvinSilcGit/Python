# Source https://www.techiedelight.com/find-maximum-length-sub-array-having-given-sum/

## Fix this code. Isn't working as supposed to be

import random

counter1, counter2, sum, array, randomLen, subArray = 0, 1, 0, [], [], []

goal = random.randint(1, 30)

for counter in range(15):

    randomLen.append(random.randint(1, 15))

    if randomLen[counter] in array:

        continue

    else:

        array.append(randomLen[counter])

sum = array[counter1]

subArray.append(array[counter1])

while counter1 != len(array) - 1:

    if sum + array[counter2] <= goal:

        subArray.append(array[counter2])

        sum += array[counter2]

# if Sum != Goal and Array[Counter2 + 1] + Sum > Goal:

# Sum -= Array[Counter2]

    counter2 += 1

    if counter2 == len(array):

        counter1 += 1

        counter2 = counter1 + 1

        print(subArray)

        sum = array[counter1]

        subArray.append("|")

        if array[counter1] <= goal:

            subArray.append(array[counter1])

print()
print(array)
print(goal)
print(subArray)

# 24
# 2, 6, 10, 9, 11, 15, 12, 13
