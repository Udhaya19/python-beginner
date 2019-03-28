def pattern_program():
    number = 5
    for row in range(0, number):
        for column in range(0, row + 1):
            print("*", end='')

        print(" ")


pattern_program()

