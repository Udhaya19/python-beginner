def fibonacci_series(number):
    first_number = 0
    second_number = 1
    fibonacci_value = []
    sum_value = 0
    for row in range(0, number):
        result = first_number + second_number
        second_number = first_number
        first_number = result
        cube_number = result ** 3
        fibonacci_value.append(cube_number)
    print(fibonacci_value)
    for value in range(0, len(fibonacci_value)):
        sum_value = sum_value + fibonacci_value[value]
    print(sum_value)


number = 5
fibonacci_series(number)
