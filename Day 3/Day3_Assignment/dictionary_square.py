def find_square_dictionary():
    num = int(input("Enter the number"))
    my_dict = {i:i * i for i in range(1, num + 1)}
    print(my_dict)


find_square_dictionary()
