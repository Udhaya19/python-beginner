def pattern_program():
    number = 5
    for row in range(0, number):
        for spaces in range(1, number * 2 - (row + 2)):
            print(" ", end=' ')
        for stars in range(0, row + 1):
            print("*", end=' ')
        print(" ")


pattern_program()
