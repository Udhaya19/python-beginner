def pattern_program():
    number = 5
    for row in range(0, number):
        for spaces in range(1, number - row):
            print(" ", end='')
        for star in range(0, row):
            print("* ", end='')
        print("*", end='')
        print(" ")

pattern_program()
