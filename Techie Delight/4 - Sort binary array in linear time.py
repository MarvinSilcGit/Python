# Source https://www.techiedelight.com/sort-binary-array-linear-time/

import random

array_0, array_1, og_array, joint_array, numero = [], [], [], [], 0

for counter in range(0, random.randint(5, 30)):

    numero = random.randrange(0, 2)

    og_array.append(numero)

    array_0.append(numero) if numero == 0 else array_1.append(numero)

joint_array = array_0 + array_1

print("The original Array is: ", og_array)

print("The new Array sorted in Binary: ", joint_array)