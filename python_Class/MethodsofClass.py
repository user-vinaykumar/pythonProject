# class methods, instance methods and static methods of python classes.

class Student:

    internal_marks = 20

    def __init__(self, name, branch, id, marks, location):
        self.name = name
        self.branch = branch
        self.id = id
        self.marks = marks
        self.location = location

    def studentInfo(self):
        return (f'student name {self.name} \n'
                f'student branch {self.branch} \n '
                f'student id {self.id} \n '
                f'student marks {self.marks} \n '
                f'student location {self.location}')

    @classmethod
    def set_InternalMarks(cls, marks):
        cls.internal_marks = marks
        return cls.internal_marks

    @classmethod
    def set_student_instance(cls, info):
        fullname, branch, identitycard, marks, location = info.split(',')
        return cls(fullname, branch, identitycard, marks, location)

    @staticmethod
    def percentage(item1, item2):
        percent = float((int(item1) + item2)/100 * 100)
        return percent


vinay = Student('vinay', 'cse', 67, 79, 'Mandya')
sharan = Student('sharan', 'civil', 54, 88, 'Mysuru')

print(vinay.studentInfo())
Student.set_InternalMarks(23)
print(vinay.set_InternalMarks(24))

vinaystring = 'vinaykumar,mech,66,87,bengaluru'
vinaycls = Student.set_student_instance(vinaystring)
print(vinaycls.studentInfo())
print(f'--------------------------')
print(vinaycls.percentage(vinaycls.marks, vinaycls.internal_marks))
print(f'------------------')
print(sharan.studentInfo())
print(f'----------------------')
print(sharan.percentage(sharan.marks, sharan.set_InternalMarks(25)))
print(vinay.internal_marks)
print(Student.internal_marks)

newstring = 'rajeshwari,info_science,50,99,jeegundipatna'
rajeshwariinstance = Student.set_student_instance(newstring)
print(rajeshwariinstance.percentage(rajeshwariinstance.marks,
                                    rajeshwariinstance.internal_marks))



