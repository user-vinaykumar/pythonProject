


# importing calender library to calculate whether a given year is leap or not.

import calendar


def leapCheck(item):
    year = calendar.isleap(item)
    if year:
        print(f'the year {item} is a leap Year.')
    else:
        print(f'the year {item} is not a leap year.')


leapCheck(2018)
