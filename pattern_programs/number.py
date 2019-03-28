number = 10
space = 0

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

#   c
#  ccc
# ccccc
#  ccc
#   c

for row in range(0, number - 1):
    for spaces in range(0, (number - row - 1)):
        print("-", end='-')
    for star in range(0, (row * 2) + 1):
        print("*", end='')
        if star != (row * 2):
            print("-", end='')

    for spaces in range(0, (number - row-1)):
        print("-", end='-')
    print()


for i in range(number * 2 - 1, 0, -2):
    for spaceChar in range(0, space):
        print("-", end='-')
    for star in range(0, i):
        print("*", end='')
        if i - star != 1:
            print("-", end='')

    for spaceChar in range(0, space):
        print("-", end='-')
    space = space + 1

    print()
