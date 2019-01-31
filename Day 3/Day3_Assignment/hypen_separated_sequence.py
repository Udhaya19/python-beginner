string = input("Enter the hypen-separated-sequence")
words = string.split("-")
print("-".join(sorted(list(words))))
