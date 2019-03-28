


def split_function(dict):
    no_of_person = 5
    arr = []
    string1 = input("Enter the element")

    split1 = string1.split(",")
    for i in split1:
        if arr[i] == dict.keys():
            dict.update(arr[i + 1])
            print(dict)

split_function({'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0})
