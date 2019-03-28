def number_order(number):
    list_value = list(map(int, str(number)))
    sorted_list = list_value.copy()
    sorted_list.sort()

    if list_value == sorted_list:
        print("The given number {} is Ascending Order".format(number))
    if list_value == sorted_list[::-1]:
        print("The given number {} is Descending Order".format(number))
    if list_value != sorted_list and list_value != sorted_list[::-1]:
        print("The given number {} is Neither".format(number))


number1 = 12345
number2 = 54321
number3 = 749003
number_order(number1)
number_order(number2)
number_order(number3)
