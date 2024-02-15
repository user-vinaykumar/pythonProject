# find whether the month number of the year is even or odd using fmod function.

import math


def fmod(number, j):
    return math.fmod(number, j)


month_number = {'January': 1,
                'February': 2,
                'March': 3,
                'April': 4,
                'May': 5,
                'June': 6,
                'July': 7,
                'August': 8,
                'September': 9,
                'October': 10,
                'November': 11,
                'December': 12}


def isMonth(month_num):
    if fmod(month_number[month_num], 2) == 0:
        return 'The month is Even Month!'
    else:
        return 'The month is Odd Month!'


print(isMonth('January'))
print(isMonth('February'))
