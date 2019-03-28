number = str(input("Enter the vampire number:"))
number_length = len(number)
half_length = number_length // 2
digits = list(str(number))
possible_half_len_numbers = []
possible_len = set()

print(digits)

for i in range(0, number_length):
    for j in range(1, number_length):
        num_original = int(digits[i] + digits[j])
        if len(str(num_original)) == half_length:
            possible_half_len_numbers.append(num_original)
        num_reverse = int(digits[j] + digits[i])
        if len(str(num_reverse)) == half_length:
            possible_half_len_numbers.append(num_reverse)
        for item in possible_half_len_numbers:
            possible_len.add(item)
print(possible_len)
list_length = len(possible_len)
for i in range(0, list_length):
    for j in range(1, list_length):
        value = int(list(possible_len)[i] * list(possible_len)[j])
        if value == int(number):
            print(
                "It is vampire number,The fangs {} and {} vampire number = {}".format(list(possible_len)[i], list(possible_len)[j], number))
