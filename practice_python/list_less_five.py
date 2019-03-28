def less_five():
    list1 = []
    user_list = []
    for i in range(0, 7):
        get_value = int(input("Enter the number:"))
        user_list.append(get_value)
    print("The user entered value:", user_list)
    for i in range(0, len(user_list)):
        if user_list[i] < 5:
            list1.append(user_list[i])
    print("The list with less than five:", list1)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_five()
