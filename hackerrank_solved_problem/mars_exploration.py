def mars_exploration(string):
    count = 0
    length_string = []
    list_string = list(map(str, str(string)))
    print(list_string)
    length = len(list_string)//3
    start = 0
    end = 3
    for i in range(length):
        length_string.append(list_string[start:end])
        start = start + 3
        end = end + 3
    print(length_string)
    for j in range(0, len(length_string)):
        temp = length_string[j]
        if temp[0] != 'S':
            count = count + 1
        if temp[1] != 'O':
            count = count + 1
        if temp[2] != 'S':
            count = count + 1
    return count


# first_half = list_string[:len(list_string) // 3]
# print(first_half)
# second_half = list_string[len(list_string) // 3:]
# print(second_half)
# if list_string[:len(list_string) // 2] == list_string[len(list_string) // 2:]:
#     return 0
# for letter in range(0, len(first_half)):
#     if first_half[letter] != second_half[letter]:
#         count = count + 1
# return count


given_string = "SOSOSOSOSDSDSKWOSDOSDOASDOASDFAFJDFDOSOSOWNSOSOSNDSKDDOSOSOSJDSDSOOSOSDSDOSASSOASDSAOSOSODSDSOASDWS"
print(mars_exploration(given_string))
