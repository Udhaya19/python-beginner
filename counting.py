list1 = [-1, 0, 0, 1, 100]
positive_count = 0
negative_count = 0
zero = 0
for i in list1:
    if i == 0:
        zero += 1
    elif i < 0:
        negative_count += 1
    else:
        positive_count += 1
print("Zero count", zero)
print("Negative count", negative_count)
print("Positive count", positive_count)
