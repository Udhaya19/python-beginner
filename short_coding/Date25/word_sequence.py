def sequence_words(given_string):
    separated_string = given_string.split(",")

    separated_string.sort()

    string_result = ",".join(separated_string)
    print(string_result)


given_string = "wishes,i,bought,good"
sequence_words(given_string)

