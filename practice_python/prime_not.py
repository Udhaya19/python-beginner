def primality_program():
    number = int(input("Enter the number:"))
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("not prime number")
                break
        else:
            print("Prime number")

    else:
        print("not prime number")


primality_program()
