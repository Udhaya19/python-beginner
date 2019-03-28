def finding_character(string, number):
    lower_string = string.lower()
    split_string = lower_string.split(',')
    print(split_string)
    dict = {}
    for letter in split_string:
        dict[letter] = split_string.count(letter)

    for key in dict:
        if dict[key] == number:
            print("{}".format(key))


string = "A,b,c,a,b,b,d,d,c"
number = 2
finding_character(string, number)
