def anagram(string1, string2):
    if sorted(string1.replace(" ", "")) == sorted(string2.replace(" ", "")):
        print(True)
    else:
        print(False)


given_string1 = "astronomer"
given_string2 = "moon starer"
s1 = "banana"
s2 = "aannabb"
anagram(given_string1, given_string2)
anagram(s1,s2)
