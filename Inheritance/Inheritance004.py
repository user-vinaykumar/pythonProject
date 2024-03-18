# concepts of Inheritance and its sub categories.

class Student:
    internal_marks = 25
    def __init__(self, name, branch, id, section, college, subjects=None):
        self.name = name
        self.branch = branch
        self.id = id
        self.section = section
        self.college = college
        if subjects is None:
            self.subjects = []
        else:
            self.subjects = subjects


    def studentInfo(self):
        return (f'student name : {self.name} \n '
                f'student college : {self.college} \n'
                f'student branch : {self.branch} \n '
                f'student id : {self.id}\n'
                f'student subjects are : {self.subjects}')

    def studentName(self):
        return f'student name is : {self.name}'

    def studentBranch(self):
        return f'student branch is : {self.branch}'

    def studentid(self):
        return f'student ID is : {self.id}'

    def studentsubjects(self):
        return f'student subjects are : {self.subjects}'

class CSE_students(Student):
    interanl_marks = 20
    def __init__(self, name, branch, id, section, college, branchcode, subjects=None):
        super().__init__(name, branch, id, section, college, subjects)
        self.branchcode = branchcode

    def branch_code(self):
        return f'branch code of CSE is : {self.branchcode}'

    @classmethod
    def set_interal_marks(cls, imarks):
        cls.interanl_marks = imarks

    @staticmethod
    def examMarks(item1, item2): # item1 = internal marks, item2 = externally entered exam marks
        score = item1 + item2
        return score

class Civil(CSE_students):
    internal_marks = 30
    def __init__(self, name, branch, id, section, college, branchcode, subjects=None):
        super().__init__(name, branch, id, section, college, branchcode, subjects)

class Mechanical(CSE_students):

    internal_marks = 50
    def __init__(self, name, branch, id, section, college, branchcode, subjects=None):
        super().__init__(name, branch, id, section, college, branchcode, subjects)

jeevan = Mechanical('Jeevan', 'Mechanical', 23,
                    'B', 'Ghousia College of Engineering',
                    'ME001', )
mahesh = Civil('Mahesh Kumar', 'Civil', 42, 'A',
               'Ghousia College of Engineering', 'CV001', )

sachin = Civil('Sachin', 'Civil', 77, 'A',
               'Ghousia College of Engineering', 'CV001', )

chandan = Civil('Chandan', 'Civil', 9, 'A',
                'Ghousia College of Engineering', 'CV001', )

vinay = CSE_students('Vinay Kumar', 'Computers', 67, 'A',
                     'Ghousia College of Engineering', 'CS001', )









