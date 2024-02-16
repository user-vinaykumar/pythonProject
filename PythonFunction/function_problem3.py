# write a program that counts the number of lowercase and uppercase charecters in
# a string and store the uppercase and lowercase in dictionary inside function.

string = input('Enter any string : ')


def casecounter(item):
    dictionary = {'UPPER_CASE': 0, 'LOWER_CASE': 0}
    for charecter in item:
        if charecter.isupper():
            dictionary['UPPER_CASE'] += 1
        elif charecter.islower():
            dictionary['LOWER_CASE'] += 1
        else:
            pass

    print(f"The count of Uppercase in the given string is : {dictionary['UPPER_CASE']}")
    print(f"The count of Lowercase in the given string is : {dictionary['LOWER_CASE']}")


casecounter(string)
