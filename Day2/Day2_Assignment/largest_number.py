def create_list():
    list1 = []
    number1 = int(input("Enter the number of value in list "))
    for i in range(0, number1):
        list_number = int(input("Enter the number"))
        list1.append(list_number)
    print(list1)
    return list1


def max_number(list1):
    max = list1[0]
    for num in list1:
        if num >= max:
            max = num
    print("The given list maximum number is",max)
    return max


list1 = create_list()
max_number(list1)
