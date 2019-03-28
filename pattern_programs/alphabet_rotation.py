number = 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----


for row in range(number, 0, -1):
    for alphabet in range(row, number + 1):
        print(alphabet, end='')
    print()
