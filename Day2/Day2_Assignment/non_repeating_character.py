string = input("Enter the string:")
num = len(string)


def non_reapeating_char():
    for i in range(0, num + 1):
        if i == 0:
            if string[i] != string[i + 1]:
                print(string[i])
                break
        elif i == num + 1:
            if string[i] != string[i - 1]:
                print(string[i])
                break
        else:
            if string[i] != string[i + 1] and string[i] != string[i - 1]:
                print(string[i])
                break


non_reapeating_char()
