def create_list():
    list1 = []
    num=int(input("Enter the loop number to repeat"))
    for i in range(0, num):
        list_number = int(input("Enter the number"))
        list1.append(list_number)
    print(list1)
    return list1


def sum_even(list1):
    sum = 0
    for i in list1:
        if i % 2 == 0:
            sum += i
    print(sum)


list1 = create_list()
sum_even(list1)
