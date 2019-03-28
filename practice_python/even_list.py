def even_list():
    user_list1 = []
    even_value = []
    for i in range(0, 8):
        get_list1_value = int(input("Enter the list1 value:"))
        user_list1.append(get_list1_value)
        if user_list1[i] % 2 == 0:
            even_value.append(user_list1[i])
    print("The list1 value:", user_list1)
    print("The even value in list", even_value)


even_list()
