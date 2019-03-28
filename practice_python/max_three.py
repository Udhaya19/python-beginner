def maximum_three():
    first_value = int(input("Enter the first value:"))
    second_value = int(input("Enter the second value:"))
    third_value = int(input("Enter the third value:"))
    if first_value > second_value and first_value > third_value:
        print("The largest value is", first_value)
    elif second_value > third_value:
        print("The largest value is", second_value)
    else:
        print("The largest value is", third_value)


maximum_three()
