def string_alphabet_order():
    string = str(input("Enter the string"))
    word = sorted(string)
    print(word)
    list1 = []
    for i in string:
        list1.append(i)
    if string == word:
        print("True")
    else:
        print("False")


string_alphabet_order()
