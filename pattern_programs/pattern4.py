def pattern_program():
    number = 5
    for row in range(0, number):
        for spaces in range(0, row):
            print(" ", end='')
        for stars in range(0, number - row):
            print("* ", end='')
        print("")

pattern_program()
