def odd_even():
    number = int(input("Enter the number:"))
    check_divide = int(input("Enter the number for check divide:"))
    if number % 4 == 0:
        print("The given number is divisible by 4")
    elif number % 2 == 0:
        print("The given number is even")
    else:
        print("The given number is odd")

    if number % check_divide == 0:
        print("The number is divide by check value")
    else:
        print("The number is not divide")


odd_even()
