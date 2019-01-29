num = int(input("Enter the number"))
for outer in range(1, num + 1):
    for inner in range(1, outer + 1):
        print("#", end=" ")
    print()
