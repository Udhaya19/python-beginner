def divisors():
    number = int(input("Enter the number"))
    list1 = []
    for i in range(1, 100):
        if number % i == 0:
            list1.append(i)
    print(list1)


divisors()
