def utopian_tree(n):
    height = 1
    for i in range(0, len(n)):
        if n[i] == 0:
            height = 1
            print(height)
        elif n[i] % 2 == 0:
            height *= 2
            print(height)
        else:
            height += 1
            print(height)


n = [0, 1, 4]
utopian_tree(n)
