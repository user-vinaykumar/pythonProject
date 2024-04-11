from functools import singledispatch, singledispatchmethod

class Employee:

    @singledispatchmethod
    def display(self, pay, verbose=False):
        if verbose:
            print(f'the pay is : {pay}')
            return

        print(pay)

    @display.register
    def _(self, arg1, verbose=False):
        if verbose:
            print(f'the number: {arg1}')
            return

        print('number: ', arg1)

    @display.register
    def _(self, arg2, verbose=False):
        if verbose:
            print(f'the text: {arg2}')
            return

        print(f'text :', arg2)

emp = Employee()

emp.display(10, True)
