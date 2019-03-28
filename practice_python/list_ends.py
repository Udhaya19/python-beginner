def list_ends():
    user_list = []
    result_list = []
    for i in range(0, 8):
        get_list_value = int(input("Enter the list value:"))
        user_list.append(get_list_value)
    print(user_list)

    result_list.append(user_list[0])
    result_list.append(user_list[-1])
    print(result_list)


list_ends()
