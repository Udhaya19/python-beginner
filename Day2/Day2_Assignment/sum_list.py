def create_list():
    list1 = []
    number1 = int(input("Enter the number of value in list "))
    for i in range(0, number1):
        list_number = int(input("Enter the number"))
        list1.append(list_number)
    print(list1)
    return list1


def sum(numbers):
    sum = 0
    for iteration in numbers:
        sum += iteration
    return sum


list1 = create_list()
print(sum(list1))
