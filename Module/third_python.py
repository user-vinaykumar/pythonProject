# importing more than one feature from the other module by separating with the ' , '

from Python_module import indexfinder, variable

names = ['vinay', 'sharan', 'rajeshwari', 'shivalingaiah', 'mandya']

indx = indexfinder(names, 'rajeshwari')
print(f'the index of the value rajeshwari is : {indx}')

print('--------------------')

print(variable)