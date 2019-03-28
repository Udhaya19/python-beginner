def age_calculation():
    user_name = str(input("Enter the name:"))
    user_age = int(input("Enter the age:"))
    current_year = 2019
    age_difference = 100 - user_age
    print(age_difference)
    turn_hundred = current_year + age_difference
    print(turn_hundred)
    print("The user turn hundred in the year of", turn_hundred)


age_calculation()
