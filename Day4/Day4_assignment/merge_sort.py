def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def mergesort(list_array):
    if (len(list_array) == 1):
        return list_array
    mid = int(len(list_array) / 2)
    left = mergesort(list_array[:mid])
    right = mergesort(list_array[mid:])
    return merge(left, right)


arr = [1, 2, 4, 3, 8, 7]
print(mergesort(arr))
