# Source: https://www.techiedelight.com/check-subarray-with-0-sum-exists-not/

import random

counter, arrLen, zeroSum, zeroSum1, zeroSum2, subArr0, subArr1, subArr2, masterArr = 0, 15, 0, 0, 0, [], [], [], []

while counter != arrLen//3:

    subArr0.append(random.randint(-30, 30))

    subArr1.append(random.randint(-30, 30))

    subArr2.append(random.randint(-30, 30))

    counter += 1

    if counter == arrLen//3:

        masterArr.append(subArr0)

        masterArr.append(subArr1)

        masterArr.append(subArr2)

        for Counter1 in range(len(masterArr[0])):

            zeroSum += masterArr[0][Counter1]

        for Counter2 in range(len(masterArr[1])):

            zeroSum1 += masterArr[1][Counter2]

        for Counter3 in range(len(masterArr[2])):

            zeroSum2 += masterArr[2][Counter3]

print(masterArr)

print()

if zeroSum == 0:

    print("The Subarray", masterArr[0], "is sum 0")

elif zeroSum1 == 0:

    print("The Subarray", masterArr[1], "is sum 0")

elif zeroSum2 == 0:

    print("The Subarray", masterArr[2], "is sum 0")

elif zeroSum == 0 and zeroSum1 == 0 and zeroSum2 == 0:

    print("All the Subarrays are sum 0")

elif zeroSum + zeroSum1 + zeroSum2 == 0:

    print("The Array is sum 0")

else:

    print("There's no 0 sum")
