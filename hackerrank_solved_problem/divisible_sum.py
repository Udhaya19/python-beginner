n = 6
k = 3
array = [1, 3, 2, 6, 1, 2]


def divisible_pairs():
    count = 0
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if (array[i] + array[j]) % k == 0:
                count += 1
    return count


print(divisible_pairs())
