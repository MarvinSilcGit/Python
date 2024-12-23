# Source: https://www.techiedelight.com/check-subarray-with-0-sum-exists-not/

import random

Counter, ArrLen, ZeroSum, ZeroSum1, ZeroSum2, SubArr0, SubArr1, SubArr2, MasterArr = 0, 15, 0, 0, 0, [], [], [], []

while Counter != ArrLen//3:

    SubArr0.append(random.randint(-30, 30))

    SubArr1.append(random.randint(-30, 30))

    SubArr2.append(random.randint(-30, 30))

    Counter += 1

    if Counter == ArrLen//3:

        MasterArr.append(SubArr0)

        MasterArr.append(SubArr1)

        MasterArr.append(SubArr2)

        for Counter1 in range(len(MasterArr[0])):

            ZeroSum += MasterArr[0][Counter1]

        for Counter2 in range(len(MasterArr[1])):

            ZeroSum1 += MasterArr[1][Counter2]

        for Counter3 in range(len(MasterArr[2])):

            ZeroSum2 += MasterArr[2][Counter3]

print(MasterArr)

print()

if ZeroSum == 0:

    print("The Subarray", MasterArr[0], " is sum 0")

elif ZeroSum1 == 0:

    print("The Subarray", MasterArr[1], " is sum 0")

elif ZeroSum2 == 0:

    print("The Subarray",  MasterArr[2], "is sum 0")

elif ZeroSum == 0 and ZeroSum1 == 0 and ZeroSum2 == 0:

    print("All the Subarrays are sum 0")

elif ZeroSum + ZeroSum1 + ZeroSum2 == 0:

    print("The Array is sum 0")

else:

    print("There's no 0 sum")
