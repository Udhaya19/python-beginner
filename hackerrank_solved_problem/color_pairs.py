def color_pairs(string):
    list_string = list(map(str, str(string)))
    print(list_string)
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(0, len(list_string)):
        if list_string[i] == 'R':
            count1 = count1 + 1
        if list_string[i] == 'G':
            count2 = count2 + 1
        if list_string[i] == 'B':
            count3 = count3 + 1
    if count1 == count2 and count2 == count3 and count3 == count1:
        print("True")
    else:
        print("False")


string = "RGRBRG"
color_pairs(string)
