def timeInwords(h, m):
    values = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
              10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 16: 'sixteen',
              17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
              23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven',
              28: 'twenty eight', 29: 'twenty nine'}
    words = {1: "one minute past ", 15: "quarter past ", 30: "half past "}
    time_words = []
    if m in words.keys():
        time_words.append(words[m])
        time_words.append(values[h])
        return time_words
    if m == 00:
        time_words.append(values[h])
        time_words.append(" o' clock")
        return time_words
    if m == 45:
        time_words.append("quarter to ")
        time_words.append(values[h + 1])
        return time_words
    if (m >= 2 and m <= 14) or (m >= 16 and m <= 29):
        time_words.append(values[m])
        time_words.append(" minutes past ")
        time_words.append(values[h])
        return time_words
    if (m >= 31 and m <= 44) or (m >= 46 and m <= 59):
        time_words.append(values[60 - m])
        time_words.append(" minutes to ")
        time_words.append(values[h + 1])
        return time_words


h = int(input())
m = int(input())
final = timeInwords(h, m)
for i in range(0, len(final)):
    print(final[i], end='')
