def replace_occurence(given_string):
    result_string = given_string.split('%20')
    string_value = ('===').join(result_string)
    print(string_value)


given_string = "we%20use%20%%20to%20find%20remainder"
replace_occurence(given_string)

# output=	we===use===%===to===find===remainder
