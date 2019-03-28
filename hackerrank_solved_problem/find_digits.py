def find_digits(number):
    array = list(map(int, str(number)))
    count = 0
    for i in range(0, len(array)):
        if array[i] == 0:
            continue
        if number % array[i] == 0:
            count += 1

    print(count)


number = 1012
find_digits(number)
