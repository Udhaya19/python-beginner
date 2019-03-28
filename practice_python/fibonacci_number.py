def fibonacci_series():
    number = int(input("Enter the number"))
    first_value = 1
    second_value = -1

    for i in range(0, number):
        result = first_value + second_value
        second_value = first_value
        first_value = result
        print(result)


fibonacci_series()
