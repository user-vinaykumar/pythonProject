import datetime

my_date = datetime.datetime(2024, 0o1, 29, 0o6, 11, 59)
print(my_date)

sentence = '{0:%B %d, %Y} fell on {0:%A} and was the {0:j} day of the year'.format(my_date)
print(sentence)