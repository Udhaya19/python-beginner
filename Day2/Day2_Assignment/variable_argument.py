# def sum_numbers(*num):
#     number = num
#     for i in num:
#         number += 1
#     print("I am called with", number)
#
#     print("I am called with",number.count(num))
#
# sum_numbers(3, 4, 5,7,8 )
def sum_number(*number):
    print("I am called with",len(number))
sum_number(3,4,5,6)
