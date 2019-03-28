from math import ceil, sqrt


def sherlock_square(a, b):
    count = 0
    for i in range(a, b + 1):
        square_number = sqrt(i)
        if square_number == ceil(square_number):
            count = count + 1
    print(count)


sherlock_square(3, 9)
