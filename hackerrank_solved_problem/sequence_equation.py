def sequence_equation():
    p = []
    array = [2, 3, 1]
    for row in range(len(array)):
        i = row + 1
        first_index = array.index(i)
        second_element = array.index(first_index + 1)
        result = second_element + 1
        p.append(result)
    print(p)


sequence_equation()
