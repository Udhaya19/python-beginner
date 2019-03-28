original_number = int(input("Enter the number:"))
# number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
dup_number = list(str(original_number))
# dup_multiply_two = list(str(multiply_two))
# dup_multiply_three = list(str(multiply_three))
for i in range(0, len(dup_number) - 1):
    if dup_number[i] == '0':
        del dup_number[i]
print(dup_number)
original_number = ''
original_number = int(original_number.join(dup_number))
print(original_number)
multiply_two = original_number * 2
multiply_three = original_number * 3
fascinating_number = str(original_number) + str(multiply_two) + str(multiply_three)
print(str(fascinating_number))

fascinate_list = list(str(fascinating_number))
fascinate_list.sort()
print(fascinate_list)

if fascinate_list[0] == '0':
    print("Not Fascinate number")
else:
    print("Fascinate number")
