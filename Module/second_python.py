# importing the function name itself rather than importing an entire module.

from Python_module import indexfinder

courses = ['vinay', 'sharan', 'rajeshwari', 'shivalingaiah', 'mandya']

indx = indexfinder(courses, 'rajeshwari')
print(f'the index of the value of element rajeshwari is : {indx}')

# since we have imported only a indexfinder() function we cannot use other variables
# that are available in the Python_module