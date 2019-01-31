d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
def combine_dict():
    my_dict = {}
    my_dict = d1.copy()
    for i in my_dict:
        if i in d2:
            my_dict[i] += d2[i]
        for i in d2:
            if i not in my_dict:
                my_dict[i] = d2[i]
    print(my_dict)
combine_dict()