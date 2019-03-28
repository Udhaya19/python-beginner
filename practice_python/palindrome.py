def palindrome():
    user_data = str(input("Enter the string:"))
    reverse_string = user_data[::-1]
    print("The reverse string is,", reverse_string)
    if user_data == reverse_string:
        print("The given string is palindrome")
    else:
        print("The given string is not palindrome")


palindrome()
