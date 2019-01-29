def defal_param(num1, num2=2):
    user_value = str(input("Enter the yes/no :"))
    if user_value == "yes":
        num1 = int(input("Enter the number1 "))
        num2 = int(input("Enter the number2 "))
        if num1 == num2:
            print((num1 + num2) * 2)
        else:
            print(num1 + num2)
    else:
        if num1 == num2:
            print((num1 + num2) * 2)
        else:
            print(num1 + num2)


print(defal_param(2, 3))
