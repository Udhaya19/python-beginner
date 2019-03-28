def kaprekar_number(p, q):
    # square_number = str(number ** 2)
    # print(square_number)
    # length = len(square_number)
    # print(length)
    # result = int(square_number[0:length // 2]) + int(square_number[length // 2:])
    # print(result)

    new_list = []
    for number in range(p, q + 1):
        square_number = str(number ** 2)
        if int(square_number) == 1:
            new_list.append(number)
        if len(square_number) == 1:
            continue
        if len(square_number) > 1:
            length = len(square_number)
            result = int(square_number[0:length // 2]) + int(square_number[length // 2:])
            if result == number:
                new_list.append(number)
    if len(new_list) == 0:
        print("INVALID RANGE")
    else:
        for value in new_list:
            print(value, end=' ')


p = 1
q = 100
kaprekar_number(p, q)
