def pair_value(array, sum_value):
    for first_value in range(0, len(array)):
        for second_value in range(first_value + 1, len(array)):
            if sum_value == array[first_value] + array[second_value]:
                print("first value = {} second value = {}".format(array[first_value], array[second_value]))


array = [1, 3, 7, 4, 5, 6, 2, 5, 9]
sum_value = 10
pair_value(array, sum_value)
