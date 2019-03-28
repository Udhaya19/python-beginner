def beautiful_triplets(array, d):
    new_array_list = []
    array.sort()

    for j in range(0, len(array)):
        result1 = array[j]
        result2 = array[j] + d
        result3 = array[j] + d + d
        if result1 in array and result2 in array and result3 in array:
            array_list = [result1, result2, result3]
            new_array_list.append(array_list)

    print(len(new_array_list))


d = 3
array = [1, 2, 5, 4, 7, 8, 10]
beautiful_triplets(array, d)
