def minimum_loss(price):
    minimum_difference = []
    for i in range(0, len(price)):
        for j in range(i, len(price)):
            difference = price[i] - price[j]
            if difference > 0:
                minimum_difference.append(difference)
    return min(minimum_difference)


n = 5
price = [20, 7, 3, 5]
print(minimum_loss(price))
