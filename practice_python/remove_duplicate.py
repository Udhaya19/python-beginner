def remove_duplicate():
    user_list = []
    result_list = []
    for i in range(0, 8):
        get_list_value = int(input("Enter the list value:"))
        user_list.append(get_list_value)
    print(user_list)
    for i in user_list:
        if i not in result_list:
            result_list.append(i)
    print(result_list)


remove_duplicate()
