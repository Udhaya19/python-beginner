def sum_of_digits(number):
    fact = 1
    factorial_sum = 0
    for i in range(1, number + 1):
        fact = fact * i
    print("The factorial of {} is {}".format(number, fact))
    factorial_number = list(map(int, str(fact)))
    print(factorial_number)
    for value in range(0, len(factorial_number)):
        factorial_sum = factorial_sum + factorial_number[value]
    print("The sum of factorial digits is", factorial_sum)


number = 5
sum_of_digits(number)
