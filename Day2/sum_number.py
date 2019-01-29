def sum_numbers(*num):
    print(type(num))
    sum = 0
    list1 = [1, 2, 3, 4, 5, 6]

    for i in num:
        print(type(i))
        sum += i
    print(sum)


sum_numbers(1, 2, 3)
sum_numbers([1, 2, 3])
