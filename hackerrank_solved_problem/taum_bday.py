def taum_bday(b, w, bc, wc, z):
    if ((bc + z) < wc):
        cost = (bc * b + w * (bc + z))
    elif ((wc + z) < (bc)):
        cost = (wc * w + b * (wc + z))
    else:
        cost = bc * b + wc * w
    return cost


print(taum_bday(10, 10, 1, 1, 1))
print(taum_bday(5, 9, 2, 3, 4))
print(taum_bday(3, 6, 9, 1, 1))
print(taum_bday(7, 7, 4, 2, 1))
print(taum_bday(3, 3, 1, 9, 2))
