def sock_merchant(array):
    array.sort()
    dict = {}
    for i in range(0, len(array)):
        if array[i] in dict:
            dict.pop(array[i])
        else:
            dict[array[i]] = 1
        count = len(dict)
    print(count)


array = [10, 20, 20, 10, 10, 30, 50, 10, 20]
sock_merchant(array)
