def remove_duplicate_item():
    list1 = [1,2,3,4]
    list2=[2,3,5,6]
    for list1 in list2:
        list1.append(list1.remove())
    return list1


print(remove_duplicate_item())