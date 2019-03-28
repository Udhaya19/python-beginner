def beautiful_day(i, j, k):
    count = 0
    for number in range(i, j + 1):
        reverse_number = str(number)[::-1]
        if ((number - int(reverse_number)) % k)==0:
            count = count + 1
    print(count)


i = 13
j = 45
k = 3
beautiful_day(i, j, k)
