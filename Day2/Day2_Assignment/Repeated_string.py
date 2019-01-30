def check_freq(str):
    freq = {}
    for c in str:
       freq[c] = str.count(c)
    return freq
check_freq("GOOD")