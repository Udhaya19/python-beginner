def pattern_program():
    number = 6
    letters = ['a', 'b', 'c', 'd', 'e']
    for row in range(1, number-1):
        for spaces in range(0, (number - row) - 1):
            print(" ", end='')
        for star in range(0, row):
            print("{} ".format(letters[star]), end='')
        print(" ")
    for row in range(0, number):
        for spaces in range(0, row):
            print(" ", end='')
        for star in range(0, (number - row) - 1):
            print("{} ".format(letters[star]), end='')
        print(" ")


pattern_program()
