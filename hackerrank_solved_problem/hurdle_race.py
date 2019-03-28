def hurdle_race(k, height):
    array = 0
    maximum_height = max(height)
    if maximum_height < k:
        return array
    else:
        difference = maximum_height - k
        return difference


k = 4
height = [1, 6, 3, 5, 2]
print(hurdle_race(k, height))
