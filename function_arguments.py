def fun1(*args, **kwargs):
    print(args)
    print(kwargs)

fun1('Math', 'Art', name='vinay', age=27)


print('**********************')

def fun2(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['math', 'art']
info = {'name' : 'vinay', 'age' : 28}

fun2(courses, info) # here courses and info both are considered as **args hence the
                            # output is {} in the print(**kwargs) so, we need to mention
                            # **args **kwargs
print('*******************')

fun2(*courses, **info)
