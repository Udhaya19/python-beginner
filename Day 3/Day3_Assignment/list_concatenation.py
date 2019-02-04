my_list = ['p', 'q']
num = int(input("Enter the number"))
new_list = ['{}{}'.format(i, j)for i in range(1, num + 1)for j in my_list]
print(new_list)

