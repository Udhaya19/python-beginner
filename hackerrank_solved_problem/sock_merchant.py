def sock_merchant(array):
    count = 0
    array.sort()
    dict = {}
    for i in range(0, len(array)):
        if array[i] in dict:
            dict.pop(array[i])
            count += 1
        else:
            dict[array[i]] = 1
    print(count)
    # count = 0
    # array.sort()
    # for i in range(0, len(array) - 1, 2):
    #     if array[i] == array[i + 1]:
    #         count = count + 1
    # print(count)


array = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
sock_merchant(array)
