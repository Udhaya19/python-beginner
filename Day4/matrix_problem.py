# # list1 = [[0] * 2] * 2
# # print(list1)
# # for i in range(0,3):
# #     for j in range(0,3):
# #         list1[1][2]=="*"
#
# # if list1[i][j] == list1[1][2]:
# #     print("*")
# # else:
# #     print("#")
# # print(list1)
#
#  # a = [[1, 2, 3, 4], [2, 2, 3, 4]]
#  # print("", a[0])
#
# # no_of_row = int(input("Enter the row"))
# # no_of_col = int(input("Enter the col"))
# # list1 = [[0] * no_of_row] * no_of_col
# # for i in range(0, no_of_row):
# #     for j in range(0, no_of_col):
# #         list1[i][j] == "*"
# #     print(list1[i][j])
#
# a=[[0]*3]*3
# print(a)
# a[1][2]="*"
# print()


def fill_positions(matrix_, symbol, positions):
    for position in positions:
        matrix_[position[0]][position[1]] += symbol


def common_area(matrix_, symbols):
    count = 0
    area_unit = 2
    for row in range(0, len(matrix_)):
        for column in range(0, len(matrix_[row])):
            if matrix_[row][column].strip() == symbols:
                count += 1

    return count * area_unit


number_of_rows = 3  # int(input("Enter the rows"))
number_of_columns = 3  # int(input("Enter the columns"))
matrix = [[" " for i in range(0, number_of_columns)] for y in range(0, number_of_rows)]

fill_positions(matrix, "*", [(1, 2), (0, 0)])
fill_positions(matrix, "#", [(1, 2), (0, 1)])
print(common_area(matrix, "*#"))
