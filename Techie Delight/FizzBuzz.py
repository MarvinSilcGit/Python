# Source: https://goalkicker.com/AlgorithmsBook/

Fizz, Buzz, FizzBuzz = 0, 0, 0

for Counter in range(101):

    if Counter % 3 == 0 and Counter % 5 == 0 and Counter != 0:

        Fizz += 1

        Buzz += 1

        FizzBuzz += 1

    elif Counter % 3 == 0:

        Fizz += 1

    elif Counter % 5 == 0:

        Buzz += 1

print("Has %d Fizz numbers" % Fizz)

print("Has %d Buzz numbers" % Buzz)

print("Has %d FizzBuzz numbers" % FizzBuzz)
