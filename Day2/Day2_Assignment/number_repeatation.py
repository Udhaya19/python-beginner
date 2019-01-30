number = int(input("enter the elements in list:"))
array_1 = list()
print("enter number in array:")
for i in range(0, int(number)):
    n = int(input("enter num:"))
    array_1.append(int(n))
    print("List is:", array_1)
array_1.sort()
print("sorted list is:", array_1)
for i in range(len(array_1) - 1):
    if array_1[i] == array_1[i + 1]:
        print()
        print("{} : {} times".format(array_1[i],array_1.count(array_1[i])))
