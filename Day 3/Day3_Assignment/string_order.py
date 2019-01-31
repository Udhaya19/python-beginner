def string_alphabet_order():
    string = str(input("Enter the string"))
    word = sorted(string)
    list1 = []
    for i in string:
        list1.append(i)
    if list1 == word:
        print("True")
    else:
        print("False")


string_alphabet_order()
