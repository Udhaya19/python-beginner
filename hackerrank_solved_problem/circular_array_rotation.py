def array_rotation(array, no_of_rotation, no_of_queries):
    final_value = []
    n = len(array)
    k = no_of_rotation % n
    if k != 0:
        result = array[n-k:] + array[:n-k]
        array = result
    for k in no_of_queries:
        final_value.append(array[k])
    print(final_value)


array = [1, 2, 3]
no_of_rotation = 3
no_of_queries = [0, 1, 2]
array_rotation(array, no_of_rotation, no_of_queries)
