def pair_value(array, k):
    # count = 0
    # for first_value in range(0, len(array)):
    #     for second_value in range(first_value + 1, len(array)):
    #         if k == abs(array[first_value] - array[second_value]):
    #             count = count + 1
    # print(count)

    d = {}
    answer = 0
    for i in array:
        d[i] = i
    for j in array:
        g = j + k
        if g in d:
            answer += 1
    print(answer)


array = [1, 5, 3, 4, 2]
k = 2
pair_value(array, k)
