def fatorial(n):

    if n == 0 or n == 1:

        return 1

    else:

        print(n)

        fat = n * fatorial(n - 1)

        print(n)

        print(fat)

        return fat


print(fatorial(4))
