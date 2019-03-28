def tidy_number(number):
    array = list(map(int, str(number)))
    print(array)
    copy_array = array.copy()
    copy_array.sort()
    print(copy_array)
    for value in range(0, len(array) - 1):
        if array[value] != copy_array[value]:
            return "NO"
    return "YES"


number = 1243

print(tidy_number(number))
