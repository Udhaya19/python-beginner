def list_overlap():
    user_list1 = []
    user_list2 = []
    common_value = []
    non_repeat_value = set()
    for i in range(0, 6):
        get_list1_value = int(input("Enter the list1 value:"))
        user_list1.append(get_list1_value)
    print("The list1 value:", user_list1)
    for i in range(0, 8):
        get_list2_value = int(input("Enter the list2 value:"))
        user_list2.append(get_list2_value)
    print("The list2 value:", user_list2)
    for i in range(0, len(user_list1)):
        for j in range(0, len(user_list2)):
            if user_list1[i] == user_list2[j]:
                common_value.append(user_list1[i])
    print("The common value in the two list", common_value)
    for value in common_value:
        non_repeat_value.add(value)
    print("Common non repeating value:", non_repeat_value)


list_overlap()
