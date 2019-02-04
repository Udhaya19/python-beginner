def find_caesar_cipher():
    number=int(input("Enter the number to shift"))
    character=str(input("Enter the character"))
    print(chr(ord(character)+number))
find_caesar_cipher()
