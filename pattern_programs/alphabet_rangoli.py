# 3 [e, d, c]

# def getLetters(letters, n):
#     for row in range(0, len(letters)):
#         for column in range(0, row + 1):
#             for spaces in range(0, ((n * 2) - ((row + 1) * 2))):
#                 print("-", end='')
#             # for letter in range(1, row + 2):
#             print(letters[column], end="-")
#         print("")
#
#
# letters = ['e', 'd', 'c']
# n = 3
# getLetters(letters, n)
def pattern_program():
    number = 3
    letters = ['a', 'b', 'c', 'd', 'e']
    for row in range(0, number):
        for spaces in range(0, ((number * 2) - ((row + 1) * 2))):
            print("-", end='')
        for letter in range(1, row + 2):
            print("*-", end='')
        for star in range(2, row + 2):
            print("*-", end='')

        print(" ")
#     for row in range(0, number - 1):
#         for spaces in range(0, row + 2):
#             print("-", end='')
#         for letter in range(1, ((number * 2) - ((row + 1) * 2))):
#             print("*-", end='')
#
#         print(" ")
#
#
pattern_program()
