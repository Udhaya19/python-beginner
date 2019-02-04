dictionary = {1: [1, 2, 3], 2: [1, 2, 3, 4], 3: "a"}
count = 0

for values in dictionary.values():
    if type(values) == list:
        count += 1
print(count)
