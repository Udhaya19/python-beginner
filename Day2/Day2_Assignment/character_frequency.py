string = input("Enter the string")
character = input("Enter the character")
for character in string:
    print("{} : {}".format(character, string.count(character)))
