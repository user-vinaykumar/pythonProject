# create a student class.

class Student:
    def __init__(self, name, rollNo, branch, location, result):
        self.name = name
        self.rollNo = rollNo
        self.branch = branch
        self.location = location
        self.result = result

    def marks(self):
        print(f'the mark the student is : {self.result}')

    def studentInfo(self):
        print(f'the student name is : {self.name}')
        print(f'the student roll number is : {self.rollNo}')
        print(f'the branch student belongs to : {self.branch}')
        print(f'the location the student is from : {self.location}')

vinay = Student('vinay kumar g s', 67, 'computer science',
                'Mandya', 'Pass')

vinay.studentInfo()

sharan = Student('sharan g s', 56, 'civil Engineering',
                 'Mandya', 'Pass')

jayaprakasha = Student('jayaprakasha B', 23, 'civil engineering',
                       'Ramanagara', 'Pass')
jagadeesha = Student('jagadeesha B', 27, 'computer science',
                     'Ramanagara', 'Pass')

print('-------------------')
jagadeesha.studentInfo()
print('---------------')
jayaprakasha.studentInfo()
print('-------------------------')
sharan.studentInfo()