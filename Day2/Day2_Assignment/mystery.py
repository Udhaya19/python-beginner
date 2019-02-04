def mystery_problem(num):
    sum = 1

    for i in range(1, num):
        if i < 6:
                                            # num=1 to 5: sum=2^(num^2)
            for k in range(1, num):
                sum *= 2
        else:
            if i < 10:
                                    # num=6:  sum=2^(5*num)*5
                sum *= 5
                                    # num=7:  sum=2^(5*num)*(5^2)
            else:
                              # num=8:  sum=2^(5*num)*(5^3)
                sum *= 3

                                      # num=10: sum=2^(5*num)*(5^4)*(3^1)
                                      # num=11: sum=2^(5*num)*(5^4)*(3^2)
    print(sum)
    return sum
                                    # num=12: sum=2^(5*num)*(5^4)*(3^3)


mystery_problem(4)
