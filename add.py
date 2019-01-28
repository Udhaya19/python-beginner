a = 60

while True:
    b = int(input("Enter the number"))
    if a == b:
        print("The entered number is correct")
        break

    elif b > a:
        print("The number is high..reduce the number")

    elif b < a:
        print("The number is low..increase the number")

    else:
        print("Good Luck for next time")
