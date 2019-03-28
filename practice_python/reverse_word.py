def reverse_word():
    my_string = str(input("Enter the string:"))
    split_string = my_string.split(" ")
    print(split_string)
    reverse_string = split_string[::-1]
    print(reverse_string)
    join_string = " ".join(reverse_string)
    print(join_string)


reverse_word()
