# difference in class variable and instance variable.

class Markscard:

    students_attended = 0
    internal_marks = 24

    def __init__(self, name, branch, score, percentage):
        self.name = name
        self.branch = branch
        self.score = score
        self.percentage = percentage

        Markscard.students_attended += 1

    def totalMarks(self):
        self.score+= self.internal_marks
        return self.score

    def markssheet(self):
        print(f'the name of the student is : {self.name}')
        print(f'the branch of the {self.name} is {self.branch}')
        print(f'the percentage of the {self.name} is {self.percentage}')
        self.totalMarks()

print(Markscard.students_attended)
print(f'-----------------------------')

vinay = Markscard('vinay', 'computers', 100, 78)
sharan = Markscard('sharan', 'civil', 96, 67)
amma = Markscard('amma', 'homemaking', 100, 100)



print(vinay.totalMarks())
print(sharan.totalMarks())
print(amma.totalMarks())
print(f'-----------------------')
print(f'{Markscard.students_attended}')







