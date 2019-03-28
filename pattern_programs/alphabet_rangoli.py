def pattern_program():
    number = 5
    space = 0

    for row in range(0, number + 1):
        for spaces in range(0, (number - row) + 1):
            print(" ", end='')
        for star in range(0, (row * 2) + 1):
            print("*", end='')

        print()
    for i in range(number * 2 - 1, 0, -2):
        for spaceChar in range(0, space):
            print(" ", end='')
        for star in range(0, i):
            print("*", end='')
        space = space + 1

        print()


pattern_program()
