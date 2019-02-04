# list1=[[0]*3,[0]*3]
# print(list1)
# print("Row:",len(list1))
# print("Column:",len(list1[0]))
# for i in range(0,len(list1)):
#     for j in range(0,len(list1[0])):
#         list1[i][j]=int(input("Enter the  number"))
# print(list1)
# list1[1][2]="*"
# print(list1)

# string = str(input("Enter the string:"))
# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")
# def find_occurrence_count(string):
#     occurrence = {}
#     for letter in string:
#         occurrence[letter] = string.count(letter)
#     for key in occurrence:
#         print("{}: {} times".format(key, occurrence[key]))
#
#
# find_occurrence_count(input("Enter your string"))

def find_non_repeating_character(string):
    size_ = len(string)
    for i in range(0, size_):
        if i == 0:
            if string[i] != string[i+1]:
                return string[i]
        if i == size_ - 1:
            if string[i] != string[i-1]:
                return string[i]
        else:
            if string[i] != string[i-1] and string[i]!= string[i+1]:
                return string[i]

input_string = input("Enter the string")
print(find_non_repeating_character(input_string))
