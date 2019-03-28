def nondivisible_subset(S, k):
    count = 0
    for i in range(0, len(S)):
        for j in range(i + 1, len(S)):
            if ((S[i] + S[j]) % k != 0):
                count += 1
    return count


S = [1, 7, 2, 4]
k = 3
print(nondivisible_subset(S, k))
