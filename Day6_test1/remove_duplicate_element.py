def remove_duplicate_item(elements):
    list1 = []
    for i in elements:
        if i not in list1:
            list1.append(i)
    return list1


elements = [1, 2, 3, 2, 1, 25, 6]
print(remove_duplicate_item(elements))
