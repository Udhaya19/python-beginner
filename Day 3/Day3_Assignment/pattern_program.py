num = int(input("Enter the number"))


def outer_function():
    for outer in range(1, num + 1):
        for inner in range(1, outer + 1):
            print("*", end=" ")
        print()


def inner_function():
    for outer in range(num + 1, 1, -1):
        for inner in range(1, outer - 1):
            print("*", end=" ")
        print()


outer_function()
inner_function()
