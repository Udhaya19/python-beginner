array = [1, 2, 2, 1, 4, 5]
count = 0
# for i in range(0,len(array)-1):
#     if i==array
#
# for element in array:
#     if element == value:
#         count += 1
# print(count)
# for i in range(0, len(array) - 1):
#     for j in range(0,len(array)-1):
#         if array[i] == array[j]:
#             list1.append(array.count(i))
#
#         print(list1)

count_map = {}
for i in array:
    count_map[i] = array.count(i)

print(count_map)

count_list = []
for index, element in enumerate(array):
    min_index = array.index(element)
    if min_index < index:
        continue
    count_list.append(array.count(element))

print(count_list)

count_set = set(array)
max = 0
for i in count_set:
    count_of_element = array.count(i)
    if count_of_element > max:
        max = count_of_element

