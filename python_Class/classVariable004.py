# difference in class variable and instance variable.

class Worker:

    raise_amount = 1.08
    total_emp = 0

    def __init__(self, name, salary, grade):
        self.name = name
        self.grade = grade
        self.salary = salary

        Worker.total_emp += 1

    def workerInfo(self):
        return (f'name is : {self.name} \n'
                f'salary of {self.name} is : {self.salary} \n'
                f'grade of {self.name} is : {self.grade}')

    def salary_raise(self):
        self.salary = self.salary + self.raise_amount
        return self.salary


print(Worker.total_emp)
print(f'-----------------------')


vinay = Worker('vinay', 100, 'A')
sharan = Worker('sharan', 50, 'B')
vinaykumar = Worker('vinaykumar', 20, 'C')

print(f'---------------------')
print(f'{Worker.total_emp}')

print(f'------------------')

print(f'{vinaykumar.salary_raise()}')
print(f'{vinay.salary_raise()}')
print(f'{sharan.salary_raise()}')
print(f'------------------')

print(f'{vinay.workerInfo()}')
print(f'{sharan.workerInfo()}')
print(f'{vinaykumar.workerInfo()}')


