# write a function to check the number of days present in a given month.

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        print('Invalid Month!')
    if month == 2 and is_leap(year):
        return 29

    return month_days[month-1]

print(days_in_month(2014, 2))

