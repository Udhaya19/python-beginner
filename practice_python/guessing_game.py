def guessing_number():
    number = 6
    count = 0
    while True:
        guess_number = int(input("Enter the guessing number:"))
        if number == guess_number:
            print("The entered number is correct")
            break

        elif guess_number > number:
            print("The number is high..reduce the number")
            count += 1

        elif guess_number < number:
            print("The number is low..increase the number")
            count += 1
        else:
            print("Good Luck for next time")
    print("The count of user guessing", count)


guessing_number()
