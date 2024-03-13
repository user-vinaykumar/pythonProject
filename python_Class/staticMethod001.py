# static method example is shown here in this.

class Employee:

    def percentage(self):  # instance methods will take self as their first argument.
        pass

    @classmethod
    def network(cls):  # class methods will take cls as their first argument.
        pass

    @staticmethod
    def is_weekdaY(day):  # static methods neither take self nor cls as their arguments but receive what is given.
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_date = datetime.datetime(2023, 3, 13)
print(Employee.is_weekdaY(my_date))