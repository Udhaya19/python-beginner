def element_search(array, search_element):
    for i in range(0, len(array)):
        if array[i] == search_element:
            return True

    return False


array = [1, 2, 3, 4, 9]
search_element1 = 4
search_element2 = 10
print(element_search(array, search_element1))
print(element_search(array, search_element2))
